const asyncHandler = require('express-async-handler');
const { Configuration, OpenAIApi } = require('openai');
const { Message } = require('../models/chatbotModels');
const prompts = require('../utils/prompts');
const { Session } = require('../models/chatbotModels');

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

// send message to chatbot
// send message to chatbot
const sendMessage = asyncHandler(async (req, res, shouldReturn = false) => {
    try {
        // get relevant data from request body
        const { message, role, sessionId } = req.body;

        console.log('session_id: ' +  sessionId);

        const session = await Session.findById(sessionId);
    
        // check if session exists
        // ERROR HERE
        if (!session) {
            return res.status(404).json({ message: 'Session not found' });
        }
    
        // check if message is empty
        if (!message || message.length === 0 || typeof message !== 'string') {
            return res.status(400).json({message: 'Message format is not valid' });
        }
    
        // check if role is valid
        if (!role || (role !== 'user' && role !== 'system')) {
            return res.status(400).json({ message: 'Role is not valid' });
        }

        let messageLog = session.messageLog;

        // send the model to the AI backend
        const aiModel = openai.createChatCompletion({
            model: 'gpt-4',
            messages: messageLog,
            temperature: 0.7,
            max_tokens: 250,
        });

        const response = await aiModel;
        const aiResponse = response.data.choices[0].message.content;
        if (role === 'user') {
            messageLog.push({role: role, content: message});
            messageLog.push({role: 'assistant', content: aiResponse});
        } else if (role === 'system') {
            messageLog.push({role: role, content: message});
        }

        // Update the messageLog in the session
        session.messageLog = messageLog;
        await session.save();

        const parentMessage = await Message.findOne({ session_id: sessionId }).sort('-createdAt');
        const choices = await generateChoices(aiResponse);

        // create a message object
        const msg = new Message({
            session_id: sessionId,
            role: role,
            content: message,
            response: aiResponse,
            choices: choices,
            parent: parentMessage ? parentMessage._id : null,
        });
        
        // save the message
        const savedMsg = await msg.save();

        // update the children node field of the parent message
        if (parentMessage) {
            parentMessage.children.push(savedMsg._id);
            await parentMessage.save();
        }

        if (res === undefined) {
            return savedMsg;
        }
        if (shouldReturn) {
            return {
                message: msg,
                session
            };
        } else {
            // return the message object
            res.status(201).json(msg);
        }

    } catch (error) {
        console.log(error);
        return res.status(500).json({ message: 'Error in sending message to server' });
    }
});


// get all messages associated with a session
const getMessages = asyncHandler(async (req, res) => {
    try {
        // get all messages from the server from the session
        const messages = await Message.find({ session_id: req.params.session_id });

        // check if messages exist
        if (!messages || messages.length === 0) {
            res.status(404).json({ message: 'No messages found for this session' });
            return;
        }

        // return the messages
        res.status(200).json(messages);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Server error' });
    }
});

// update message
const updateMessage = asyncHandler(async (req, res) => {
    // get the new message from the request body and create a child for the message_id's parent node
    // basically creating a new branch in the message tree
    try {
        const { message_id } = req.params;
        const { message } = req.body;
        const messageToUpdate = await Message.findById(message_id);

        if (!messageToUpdate) {
            return res.status(404).json({ message: 'Message not found' });
        }
    
        const newMsg = await sendMessage({message: message, role: 'user', sessionId: messageToUpdate.session_id}, res);
        
        // add newMsg as a child reference to the parent message
        messageToUpdate.children.push(newMsg._id);

        // make the parent message the parent reference to the new message
        newMsg.parent = messageToUpdate._id;

        // save the updated message
        const updatedMsg = await messageToUpdate.save();

        // find session and update messageLog
        const session = await Session.findById(messageToUpdate.session_id);

        // use reverse dfs to update messageLog
        let newMessageLog = [];
        let tempMsg = newMsg;

        while (tempMsg) {
            newMessageLog.push({role: tempMsg.role, content: tempMsg.content});
            tempMsg = await Message.findById(tempMsg.parent);
        }

        // update the messageLog in the session and save
        session.messageLog = newMessageLog.reverse();
        await session.save();
        
        // return the new message
        return res.status(200).json(newMsg);

    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'Error in updating message from server' });
    }
});

// get message by id
async function getMessageById(req, res) {
    try {
        // get the message id from the url
        const { message_id } = req.params;
        
        // using the id retrieve the message
        const message = await Message.findById(message_id);

        if (!message) {
            return res.status(404).json({ message: 'Message not found' });
        }

        // return the message object
        return res.status(200).json(message);

    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'Error in retrieving message from server' })
    }
};

// generate choices
async function generateChoices(aiResponse) {
    try {
        // use the AI backend to generate choices to further the story
        const aiModel = openai.createChatCompletion({
            model: 'gpt-4',
            messages: [{'role':'system', 'content': prompts.choicePrompt}, {'role': 'user', 'content': aiResponse}],
            temperature: 0.7,
            n: 4,
        });

        // get the choices from the AI backend
        const response = await aiModel;
        
        let choices = [];
        response.data.choices.forEach(choice => {
            const textResponse = choice.message.content;

            // check if choices are returned in the response
            if (!textResponse.includes('CHOICES')) {
                throw new Error('AI model did not generate choices as expected');
            }

            // clean the choices and return as a list
            const ch = textResponse.split('CHOICES')[1].split('\n');
            const choiceList = ch.map(c => c.trim());

            // add the choices to the overall choices array
            choices = [...choices, ...choiceList];
        });

        return choices;
    } catch (error) {
        console.log(error);
        throw new Error('Error in generating choices from the AI backend');
    }
};

module.exports = {
    sendMessage,
    updateMessage,
    getMessages
};
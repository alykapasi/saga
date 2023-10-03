const asyncHandler = require('express-async-handler');
const { Configuration, OpenAIApi } = require('openai');
const { Message } = require('../models/chatbotModels');
const prompts = require('../utils/prompts');
const { sendMessage } = require('./messageController');
const { Session } = require('../models/chatbotModels');

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

const startStory = asyncHandler(async (req, res) => {
    try {
        // handle logic for starting the conversation
        console.log(req.body);
        console.log('----------------\n');
        const { session_name, topic } = req.body;

        // check if session_name and topic are provided
        if (!session_name || !topic) {
            return res.status(400).json({ message: 'All fields are mandatory' });
        }

        // create the session
        const session = await Session.create({
            messageLog: [],
            session_name,
            topic
        });

        // const savedSession = await session.save()

        console.log('--------------\n' + session._id + '\n--------------');

        // create the first using the parts from prompts.js
        const initPrompt = prompts.setupPrompt + topic;
        
        // create the message object
        const initMessage = {
            role: 'system',
            content: initPrompt,
        };
        
        // console.log(initMessage);

        // create a new request that can be sent to sendMessage
        const newReq = {
            body: {
                message: initMessage.content,
                role: initMessage.role,
                sessionId: session._id.toString(),
            }
        };

        // use sendMessage to initialize the AI
        const initResponse = await sendMessage(newReq, res, true);

        // send back the created session
        return res.status(201).json(session);

    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'An error occurred while creating the session' });
    }
});


const getStory = asyncHandler(async (req, res) => {
    // handle logic for resuming the saved conversation

    try {
        // find the session by id
        const session = await Session.findById(req.params.session_id);

        // check if the session exists
        if (!session) {
            return res.status(404).json({ message: 'Could not find save' });
        }

        // send back the found session
        return res.status(200).json(session);

    } catch (error) {
        // log the error and send a 500 status code with an error message
        console.error(error);
        return res.status(500).json({ message: 'An error occurred while retrieving the session' });
    }
});

const saveStory = asyncHandler(async (req, res) => {
    // handle logic for saving the conversation
    try {
        const { session_id } = req.params;
        const updatedData = req.body;

        // find the session by ID and update it
        const session = await Session.findByIdAndUpdate(
            session_id,
            updatedData,
            { new: true });

        // check if the session was found and updated
        if (!session) {
            return res.status(404).json({ message: 'Session not found' });
        }

        // send back the updated session
        return res.status(200).json(session);
        
    } catch (error) {
        // log the error and send a 500 status code with an error message
        console.error(error);
        return res.status(500).json({ message: 'An error occurred while saving the session' });
    }
});

// getStories, getStory

const getStories = asyncHandler(async (req, res) => {
    // handle logic for retreiving all messages
    try {
        const sessions = await Session.find();
        res.status(200).json(sessions);
    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: 'An error occured while retrieving the sessions' });
    }
});

const deleteStory = asyncHandler(async (req, res) =>{
    // handle logic for deleting the session
    try {
        // retrieve session id using the request param
        const { session_id } = req.params;

        // delete the session by the id
        const session = await Session.findByIdAndDelete(session_id);

        // if session does not exist -> return an error message
        if (!session) {
            return res.status(404).json({ message: 'Session not found' });
        }

        // if successful, return a message
        return res.status(200).json({ message: 'Session deleted successfully' })

    } catch (error) {
        // log error and send a 500 status code with an error message
        console.error(error);
        return res.status(500).json({ message: 'An error occured while deleting the session' });
    }
});

// will need to change to do reverse-dfs
const summarizeStory = asyncHandler(async (req, res) => {
    // handle logic for summarizing the conversation
    try {
        // retrieve session ID from params
        const { session_id } = req.params;

        // find the session with given ID
        const session = await Session.findById(session_id);

        // check if session exists
        if (!session) {
            return res.status(404).json({ message: 'Session not found' });
        }

        // combine all message contents into one string
        let summary = session.messageLog.map(msg => msg.content).join(' ');

        // Use OpenAI's model to summarize the conversation
        const model = await openai.createChatCompletion({
            model: 'gpt-4-32k',
            messages: [
                {'role': 'system', 'content': 'summarize the following:\n'}, 
                {'role': 'user', 'content': summary}
            ],
            temperature: 0.75,
            max_tokens: 1000,
        });

        return res.status(200).json({ summary: model.data.choices[0].message.content })

    } catch (error) {
        // log the error and send a 500 status code with an error message
        console.error(error);
        return res.status(500).json({ message: 'An error occurred while summarizing the session' });
    }
});

module.exports = {
    startStory,
    getStories,
    getStory,
    saveStory,
    summarizeStory,
    deleteStory
}
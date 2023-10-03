const mongoose = require('mongoose');
const { Schema } = mongoose;

const SessionSchema = new Schema({
    messageLog: [
        {
            role: {
                type: String,
                required: [true, 'Please select the role of the user'],
            },
            content: {
                type: String,
                required: [true, 'Please insert output'],
            }
        }
    ],
    session_name: {
        type: String,
        required: [true, 'Please include a name for your save file'],
    },
    topic: {
        type: String,
        required: [true, 'Please select which story you would like to use']
    },
},
{
    timestamps: true,
});

const MessageSchema = new Schema({
    session_id: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Session',
        required: [true, 'Please reference the correct session id']
    },
    role: {
        type: String,
        required: [true, 'Please select the role of the user'],
    },
    content: {
        type: String,
        required: [true, 'Please insert output'],
    },
    response: {
        type: String,
        required: [true, 'Please input the generated output'],
    },
    choices: {
        type: [String],
        required: false,
    },
    parent: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Message',
        required: false,
    },
    children: {
        type: [mongoose.Schema.Types.ObjectId],
        ref: 'Message',
        required: false,
    },
},
{
    timestamps: true
});

const Session = mongoose.model('Session', SessionSchema);
const Message = mongoose.model('Message', MessageSchema);

module.exports = {
    Session,
    Message
};
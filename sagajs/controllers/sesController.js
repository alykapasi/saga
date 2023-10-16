const asyncHandler = require('express-async-handler');
const { Session } = require('../models/chatbotModels');

// creates a new session object
const startSession = asyncHandler(async (req, res) => {
    try {
        const { session_name, topic } = req.body;

        if (!session_name || !topic) {
            return res.status(400).json({
                message: 'All fields are mandatory'
            });
        }

        const session = await Session.create({
            messageLog: [],
            session_name,
            topic
        });

        return res.status(201).json({
            message: 'Session created successfully',
            session_id: session._id,
            session
        });
    }
     catch (error) {
        console.error(error);
        return res.status(500).json({
            message: 'An error occurred while creating the session'
        });
    }
});

// retrieves all sessions
const getSession = asyncHandler(async (req, res) => {
    try {
        const sessions = await Session.find();

        if (sessions.length === 0) {
            return res.status(200).json({
                message: 'No sessions found',
                sessions: []
            })
        }

        res.status(200).json({
            message: 'Sessions retrieved successfully',
            sessions: sessions.map(session => ({
                session_id: session._id,
                session
            }))
        });
    }
    catch (error) {
        console.error(error);
        return res.status(500).json({
            message: 'An error occurred while retrieving the sessions'
        });
    }
});

// retrieves a session by its id
const getSessionById = asyncHandler(async (req, res) => {
    try {
        const { session_id } = req.params;

        const session = await Session.findById(session_id);

        if (!session) {
            return res.status(404).json({
                message: 'Session not found'
            });
        }

        res.status(200).json({
            message: 'Session retrieved successfully',
            session
        });
    }
    catch (error) {
        console.error(error);
        return res.status(500).json({
            message: 'An error occurred while retrieving the session'
        });
    
    }
});

// rename the save file's name
const renameSession = asyncHandler(async (req, res) => {
    try {
        const {session_id} = req.params;
        const {session_name} = req.body;

        if (!session_name) {
            return res.status(400).json({
                message: 'New session name is required'
            });
        }

        const session = await Session.findById(session_id);

        if(!session) {
            return res.status(404).json({
                message: 'Session not found'
            });
        }

        session.session_name = session_name;
        await session.save();

        res.status(200).json({
            message: 'Session renamed successfully',
            session
        });
    }
    catch(error) {
        console.error(error);
        return res.status(500).json({
            message: 'An error occurred while renaming the session'
        });
    }
});

// delete the saved chat
const deleteSession = asyncHandler(async (req, res) => {
    try {
        const { session_id } = req.params;

        const session = await Session.findByIdAndDelete(session_id);

        if (!session) {
            return res.status(404).json({
                message: 'Session not found'
            });
        }

        res.status(200).json({
            message: 'Session deleted successfully',
            session
        });
    }
    catch (error) {
        console.error(error);
        return res.status(500).json({
            message: 'An error occurred while deleting the session'
        });
    }
});

module.exports = {
    startSession,
    getSession,
    getSessionById,
    renameSession,
    deleteSession
}
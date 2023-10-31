const express = require('express');
const router = express.Router();

const {
    startSession,
    getSession,
    getSessionById,
    renameSession,
    deleteSession
} = require('../controllers/sessionController');

const {
    sendMessage,
    getMessages,
    updateMessage
} = require('../controllers/messageController');

// route to create new story
router.route('/new')
.post(startSession);

router.route('/saves')
.get(getSession);

// save, resume a story
router.route('/:session_id')
.get(getSessionById)
.delete(deleteSession)
.post(renameSession);

// summarize a story based on session id
// router.route('/:session_id/summarize')
// .get(summarizeStory);

// rewind to a certain message
router.route('/rewind/:message_id')
.post(updateMessage);

// add message
router.route('/send_message')
.post(sendMessage);

router.route('/get_messages')
.get(getMessages);

module.exports = router;
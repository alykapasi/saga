const asyncHandler = require('express-async-handler');
const { Configuration, OpenAIApi } = require('openai');
const { Message } = require('../models/chatbotModels');
const prompts = require('../utils/prompts');
const { Session } = require('../models/chatbotModels');

const configuration = new Configuration({
    apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);
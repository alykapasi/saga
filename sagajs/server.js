require('dotenv').config();
const cors = require('cors');
const express = require('express');
const mongoose = require('mongoose');
const morgan = require('morgan');
const PORT = process.env.PORT || 5555;
const app = express();

app.use(express.json())
app.use(cors());

// connect to mongodb
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
.then(() => console.log(`Connected to MongoDB`))
.catch(err => console.log(`Unable to connect to MongoDB`, err));

// define api routes
app.use('/api/chatbot', require('./routes/chatbotRoutes'));

// start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

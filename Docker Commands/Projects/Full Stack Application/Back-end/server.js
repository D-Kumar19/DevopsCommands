const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(cors());

const mongoURI = process.env.MONGO_URI || 'mongodb://mongo:27017/submissions';
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.error('MongoDB connection error:', err));

const submissionSchema = new mongoose.Schema({
    name: { type: String, required: true },
    email: { type: String, required: true },
    dob: { type: Date, required: true }
});

const Submission = mongoose.model('Submission', submissionSchema);

app.post('/submit', async (req, res) => {
    try {
        const { name, email, dob } = req.body;
        if (!name || !email || !dob) {
            return res.status(400).send('All fields are required.');
        }
        const newSubmission = new Submission(req.body);
        await newSubmission.save();
        res.status(200).send('Submission successful');
    } catch (err) {
        console.error('Error saving submission:', err);
        res.status(500).send('Server error. Please try again later.');
    }
});

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});

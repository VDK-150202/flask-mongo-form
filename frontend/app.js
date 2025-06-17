const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/submit', async (req, res) => {
  try {
    const response = await axios.post('http://backend:5000/submittodoitem', req.body);
    res.send("Submitted to Flask: " + JSON.stringify(response.data));
  } catch (error) {
    res.send("Error: " + error.message);
  }
});

app.listen(3000, () => {
  console.log('Frontend server running on port 3000');
});

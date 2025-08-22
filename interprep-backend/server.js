// Import required packages
const express = require('express');      // Express framework to create API routes
const cors = require('cors');            // CORS middleware to allow cross-origin requests (frontend <-> backend)
const bodyParser = require('body-parser'); // Middleware to parse JSON request bodies

const app = express();                   // Initialize the Express app
const PORT = 5000;                       // Port number where the server will run

// --------------------- MIDDLEWARE ---------------------
// Enable CORS so the frontend (localhost:3000) can call this backend
app.use(cors());

// Parse incoming JSON data in request body
app.use(bodyParser.json());

// --------------------- ROUTES -------------------------

// Test route to check if backend is running
app.get('/', (req, res) => {
  res.send('InterPrep API is running!');
});

// Signup endpoint to receive user information from frontend
app.post('/api/signup', (req, res) => {
  // Destructure data from the request body
  const { name, email, interests } = req.body;
  
  // Log the received user info (for debugging purposes)
  console.log('Received user:', req.body);
  
  // TODO: Here you would normally save the user info to a database

  // Send a JSON response back to the frontend
  res.json({ 
    message: 'Signup successful', 
    user: { name, email, interests } 
  });
});

// --------------------- START SERVER ------------------
// Start listening for requests on the specified PORT
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

import React, { useState } from 'react';

function Signup() {
  // -------------------- STATE --------------------
  // Stores the input values from the form
  const [form, setForm] = useState({
    name: '',
    email: '',
    interests: ''
  });

  // -------------------- HANDLE CHANGE --------------------
  // Updates the state when user types in any input field
  const handleChange = (e) => {
    // e.target.name is the name attribute of the input
    // e.target.value is the current value
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // -------------------- HANDLE SUBMIT --------------------
  // Runs when the user clicks "Submit"
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent page reload

    try {
      // Send POST request to backend API
      const response = await fetch('http://localhost:5000/api/signup', {
        method: 'POST', // HTTP method
        headers: {
          'Content-Type': 'application/json' // Tell backend we're sending JSON
        },
        body: JSON.stringify(form) // Convert state object to JSON string
      });

      // Parse JSON response from backend
      const data = await response.json();
      console.log('Response from backend:', data); // Log for debugging

      // Show success message to user
      alert(data.message);

      // Optional: Reset the form after successful submission
      setForm({ name: '', email: '', interests: '' });

    } catch (error) {
      // Handle network errors or server errors
      console.error('Error submitting form:', error);
      alert('There was an error. Please try again.');
    }
  };

  // -------------------- RENDER FORM --------------------
  return (
    <div style={{ padding: '20px' }}>
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label><br />
          <input
            type="text"
            name="name"              // Must match state key
            value={form.name}        // Controlled component
            onChange={handleChange}  // Update state on typing
            required                 // HTML5 validation
          />
        </div>

        <div>
          <label>Email:</label><br />
          <input
            type="email"
            name="email"
            value={form.email}
            onChange={handleChange}
            required
          />
        </div>

        <div>
          <label>Interests:</label><br />
          <textarea
            name="interests"
            value={form.interests}
            onChange={handleChange}
          />
        </div>

        <button type="submit" style={{ marginTop: '10px' }}>Submit</button>
      </form>
    </div>
  );
}

export default Signup;

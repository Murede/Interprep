// src/pages/Home.js
import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Welcome to InterPrep</h1>
      <p>InterPrep helps students explore internships and create a personalized skill development plan.</p>
      <Link to="/signup">Sign Up Here</Link>
    </div>
  );
}


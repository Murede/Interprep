// src/pages/Signup.js
import React from 'react';

export default function Signup() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Sign Up</h1>
      <form>
        <input type="text" placeholder="Name" /><br /><br />
        <input type="email" placeholder="Email" /><br /><br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

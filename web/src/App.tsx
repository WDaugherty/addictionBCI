import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

// Function to call the R2R API with streaming
const callNeurosity = async (setApiRes) => {
  const apiHostname = process.env.REACT_APP_API_HOSTNAME;
  const apiUrl = apiHostname
    ? `https://${apiHostname}/api/neurosity`
    : "http://localhost:5001/api/neurosity";

  const data = { query: "Help me prevent the need to smoke again?" };
  const response = await axios.post(apiUrl, data, {
    responseType: "stream",
  });

  const reader = response.data.getReader();
  const decoder = new TextDecoder();
  let result = "";

  // Read streamed chunks
  const readChunk = async () => {
    const { done, value } = await reader.read();
    if (done) return;

    const chunk = decoder.decode(value);
    result += chunk;
    setApiRes(result); // Update the UI with the streamed data

    // Recursively read the next chunk
    readChunk();
  };

  readChunk();
};

function App() {
  const [apiRes, setApiRes] = useState("");

  const handleClick = async (e) => {
    e.preventDefault();
    await callNeurosity(setApiRes);
  };

  return (
    <div className="App">
      <header className="App-header">
        <nav>
          <div className="nav-container">
            <h1>News Site</h1>
            <ul>
              <li>Home</li>
              <li>World</li>
              <li>Politics</li>
              <li>Business</li>
              <li>Technology</li>
            </ul>
          </div>
        </nav>
      </header>
      <main>
        <div className="main-container">
          <h2>Latest News</h2>
          <button onClick={handleClick}>Get News</button>
          {apiRes && (
            <article>
              <pre>{apiRes}</pre>
            </article>
          )}
        </div>
      </main>
      <footer>
        <div className="footer-container">
          <p>&copy; 2023 News Site. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
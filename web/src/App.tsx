import React, { useState } from "react";
import axios from "axios";
import logo from "./logo.svg";
import "./App.css";

// Function to call a sample API
const callApi = async () => {
  const apiHostname = process.env.REACT_APP_API_HOSTNAME;
  const apiUrl = apiHostname
    ? `https://${apiHostname}/api/call`
    : "http://localhost:5001/api/call";
  return axios.get(apiUrl).then((resp) => resp.data);
};

// Function to call the R2R API with POST
const callR2R = async () => {
  const apiHostname = process.env.REACT_APP_API_HOSTNAME;
  const apiUrl = apiHostname
    ? `https://${apiHostname}/api/r2r`
    : "http://localhost:5001/api/r2r";
  
  // Assuming you need to send some data with the POST request
  const data = {'query': 'Help me prevent the need to smoke again?'};

  return axios.post(apiUrl, data).then((resp) => resp.data);
};

function App() {
  const [apiRes, setApiRes] = useState(-1);

  const handleClick = async (e) => {
    e.preventDefault();
    const res = await callR2R();
    setApiRes(res["random_number"]);  // Make sure to access the correct property from the response
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <button onClick={handleClick}>Call the API</button>
        </p>
        {apiRes >= 0 && <p>Result from API: {apiRes}</p>}
      </header>
    </div>
  );
}

export default App;

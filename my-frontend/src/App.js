import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLoginChange = (e) => {
    setLogin(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleLogin = (e) => {
    e.preventDefault();

    axios
      .post('http://localhost:5000/checkuser', { login, pwd: password })
      .then((response) => {
        setMessage(`Welcome ${response.data.nom} ${response.data.prenom}!`);
      })
      .catch((error) => {
        setMessage(error.response.data.message);
      });
  };

  return (
    <div className="App">
      <form onSubmit={handleLogin}>
        <label>
          Login:
          <input type="text" value={login} onChange={handleLoginChange} />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={handlePasswordChange}
          />
        </label>
        <br />
        <button type="submit">Log In</button>
      </form>
      <p>{message}</p>
    </div>
  );
}

export default App;
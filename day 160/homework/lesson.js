import React from 'react';
import './App.css';

function App() {
  const buttonStyle = {
    backgroundColor: 'blue',
    color: 'white',
    padding: '10px 20px',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer'
  };

  return (
    <div className="App">
      <h1>React Button Example</h1>

      <button style={{ backgroundColor: 'red', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>
        Inline Styled Button
      </button>

      <button style={buttonStyle}>
        Style Object Button
      </button>

      <button className="css-button">
        CSS File Button
      </button>
    </div>
  );
}

export default App;
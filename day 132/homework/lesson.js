import React, { useState } from "react";

const App = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    setCount(count + 1);
  };

  return (
    <main style={{ textAlign: "center", padding: "50px" }}>
      <h1>Counter: {count}</h1>
      <button 
        onClick={increment} 
        style={{
          padding: "10px 20px",
          fontSize: "16px",
          cursor: "pointer",
          backgroundColor: "blue",
          color: "white",
          border: "none",
          borderRadius: "5px"
        }}
      >
        Increment
      </button>
    </main>
  );
};

export default App;

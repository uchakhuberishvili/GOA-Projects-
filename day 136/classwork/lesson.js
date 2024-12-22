import React, { useState } from "react";

const RandomNumber = () => {
  const [number, setNumber] = useState(0);
  return (
    <div>
      <h1>{number}</h1>
      <button onClick={() => setNumber(Math.floor(Math.random() * 100))}>
        Generate
      </button>
    </div>
  );
};

export default RandomNumber;

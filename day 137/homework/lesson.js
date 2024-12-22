import React, { useState } from "react";

const CharCounter = () => {
  const [text, setText] = useState("");
  return (
    <div>
      <input onChange={(e) => setText(e.target.value)} />
      <h1>Characters: {text.length}</h1>
    </div>
  );
};

export default CharCounter;

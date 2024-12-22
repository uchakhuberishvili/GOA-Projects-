import React, { useState } from "react";

const Toggle = () => {
  const [on, setOn] = useState(false);
  return (
    <div>
      <h1>{on ? "ON" : "OFF"}</h1>
      <button onClick={() => setOn(!on)}>Toggle</button>
    </div>
  );
};

export default Toggle;

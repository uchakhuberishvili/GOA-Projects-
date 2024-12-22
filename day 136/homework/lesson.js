import React, { useState } from "react";

const Greeting = () => {
  const [name, setName] = useState("");
  return (
    <div>
      <input onChange={(e) => setName(e.target.value)} placeholder="Enter name" />
      <h1>{name ? `Hello, ${name}!` : "Hello!"}</h1>
    </div>
  );
};

export default Greeting;

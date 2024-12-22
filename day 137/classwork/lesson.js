import React, { useState } from "react";

const ThemeToggle = () => {
  const [dark, setDark] = useState(false);
  return (
    <div style={{ background: dark ? "#333" : "#fff", color: dark ? "#fff" : "#000" }}>
      <button onClick={() => setDark(!dark)}>Toggle Mode</button>
    </div>
  );
};

export default ThemeToggle;

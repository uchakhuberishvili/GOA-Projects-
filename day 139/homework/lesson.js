import React, { useState } from "react";

const ColorPicker = () => {
  const [color, setColor] = useState("#000000");
  return (
    <div>
      <input type="color" onChange={(e) => setColor(e.target.value)} />
      <h1 style={{ color }}>Your Color</h1>
    </div>
  );
};

export default ColorPicker;

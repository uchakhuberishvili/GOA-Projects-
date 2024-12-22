import React, { useState } from 'react';

const BackgroundColorChanger = () => {
  const [color, setColor] = useState('white');

  const changeBackgroundColor = () => {
    const colors = ['red', 'blue', 'green', 'yellow', 'orange'];
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    setColor(randomColor);
  };

  return (
    <div style={{ backgroundColor: color, padding: '50px' }}>
      <button onClick={changeBackgroundColor}>Change Background Color</button>
    </div>
  );
};

export default BackgroundColorChanger;

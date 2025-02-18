import React, { useState } from 'react';

const CounterButton = () => {
  const [count, setCount] = useState(0);
  const [checked, setChecked] = useState(false);

  const handleToggle = () => {
    setChecked(!checked);
  };

  const handleIncrement = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <Button onClick={handleIncrement}>Count: {count}</Button>
      <ToggleButton checked={checked} onChange={handleToggle} >Toggle me!</ToggleButton>
    </div>
  );
};

const ButtonList = () => {
  const [checked, setChecked] = useState(false);

  const handleToggle = () => {
    setChecked(!checked);
    console.log("Toggle button clicked!");
  };

  return (
    <div>
      <Button onClick={handleToggle}>Click me!</Button>
      <ToggleButton checked={checked} onChange={handleToggle} >Button list toggle!</ToggleButton>
    </div>
  );
};
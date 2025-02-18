import React, { useState } from 'react';

const ToggleButton = ({ children, checked, onChange }) => {
  return (
    <div>
      <input
        type="checkbox"
        checked={checked}
        onChange={onChange}
      />
      <label>{children}</label>
    </div>
  );
};

const Button = ({ children, disabled, onClick }) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
};const App = () => {
    return (
      <div>
        <CounterButton />
        <ButtonList />
      </div>
    );
  };
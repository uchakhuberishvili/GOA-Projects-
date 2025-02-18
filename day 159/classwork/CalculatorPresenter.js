import React from 'react';

function CalculatorPresenter({ num1, num2, result, onNum1Change, onNum2Change, onCalculate }) {
  return (
    <div>
      <h2>Calculator</h2>
      <div>
        <label htmlFor="num1">Number 1:</label>
        <input
          type="number"
          id="num1"
          value={num1}
          onChange={onNum1Change}
        />
      </div>
      <div>
        <label htmlFor="num2">Number 2:</label>
        <input
          type="number"
          id="num2"
          value={num2}
          onChange={onNum2Change}
        />
      </div>
      <button onClick={onCalculate}>Calculate</button>
      {result !== null && (
        <div>
          Result: {result}
        </div>
      )}
    </div>
  );
}

export default CalculatorPresenter;
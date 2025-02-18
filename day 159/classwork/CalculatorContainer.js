import React, { useState } from 'react';
import CalculatorPresenter from './CalculatorPresenter';

function CalculatorContainer() {
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [result, setResult] = useState(null);

  const handleNum1Change = (event) => {
    setNum1(event.target.value);
  };

  const handleNum2Change = (event) => {
    setNum2(event.target.value);
  };

  const handleCalculate = () => {
    const parsedNum1 = parseFloat(num1);
    const parsedNum2 = parseFloat(num2);

    if (!isNaN(parsedNum1) && !isNaN(parsedNum2)) {
      setResult(parsedNum1 + parsedNum2);
    } else {
      setResult('Invalid input');
    }
  };

  return (
    <CalculatorPresenter
      num1={num1}
      num2={num2}
      result={result}
      onNum1Change={handleNum1Change}
      onNum2Change={handleNum2Change}
      onCalculate={handleCalculate}
    />
  );
}

export default CalculatorContainer;
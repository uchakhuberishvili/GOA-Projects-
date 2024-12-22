import React, { useState } from "react";

const Calculator = () => {
  const [num1, setNum1] = useState(0);
  const [num2, setNum2] = useState(0);
  return (
    <div>
      <input type="number" onChange={(e) => setNum1(+e.target.value)} />
      <input type="number" onChange={(e) => setNum2(+e.target.value)} />
      <h1>Sum: {num1 + num2}</h1>
    </div>
  );
};

export default Calculator;

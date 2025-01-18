import React, { useState, useEffect } from 'react';

const Component = () => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log('Component rendered or re-rendered');
  }, [count]);

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => setCount(count + 1)}>Increase Count</button>
    </div>
  );
};

export default Component;

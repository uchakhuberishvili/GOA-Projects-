import React, { useState, useEffect } from 'react';
const debounce = (func, delay) => {
  let timeout;
  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), delay);
  };
};

const ResizeComponent = () => {
  const [windowSize, setWindowSize] = useState([window.innerWidth, window.innerHeight]);

  const handleResize = () => {
    setWindowSize([window.innerWidth, window.innerHeight]);
  };

  useEffect(() => {
    const debouncedResize = debounce(handleResize, 200);
    window.addEventListener('resize', debouncedResize);
    return () => {
      window.removeEventListener('resize', debouncedResize);
    };
  }, []);

  return (
    <div>
      <p>Window Width: {windowSize[0]}</p>
      <p>Window Height: {windowSize[1]}</p>
    </div>
  );
};

export default ResizeComponent;

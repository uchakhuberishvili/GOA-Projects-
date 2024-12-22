import React, { useState, useEffect } from "react";

const Timer = () => {
  const [time, setTime] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => setTime((t) => t + 1), 1000);
    return () => clearInterval(interval);
  }, []);
  return <h1>Time: {time}s</h1>;
};

export default Timer;

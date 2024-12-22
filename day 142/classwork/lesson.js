import React, { useState, useEffect } from 'react';

const WindowSizeNotification = () => {
  const [isVertical, setIsVertical] = useState(true);

  const checkWindowOrientation = () => {
    setIsVertical(window.innerWidth < window.innerHeight);
  };

  useEffect(() => {
    window.addEventListener('resize', checkWindowOrientation);
    return () => window.removeEventListener('resize', checkWindowOrientation);
  }, []);

  return (
    <div>
      <p>
        {isVertical ? 'ფანჯარა არის ვერტიკალური' : 'ფანჯარა არის ჰორიზონტალური'}
      </p>
    </div>
  );
};

export default WindowSizeNotification;

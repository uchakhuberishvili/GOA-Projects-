let countdown = 10;

const startCountdown = () => {
  const interval = setInterval(() => {
    console.log(countdown);
    countdown--;
    if (countdown < 0) {
      clearInterval(interval);
      console.log('Time is up!');
    }
  }, 1000);
};

startCountdown();

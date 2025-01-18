let countdown;

function startCountdown(seconds) {
  let remaining = seconds;
  countdown = setInterval(() => {
    console.log(remaining);
    remaining--;
    if (remaining < 0) {
      clearInterval(countdown);
      console.log("Time's up!");
    }
  }, 1000);
}

startCountdown(5);

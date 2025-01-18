let time = 10;
const timerDisplay = document.getElementById("timer");

function updateTimer() {
  timerDisplay.textContent = time;
  if (time > 0) {
    time--;
  } else {
    clearInterval(timerInterval);
  }
}

const timerInterval = setInterval(updateTimer, 1000);

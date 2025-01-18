const clockDisplay = document.getElementById("clock");

function updateClock() {
  const now = new Date();
  clockDisplay.textContent = now.toLocaleTimeString();
}

setInterval(updateClock, 1000);
updateClock();

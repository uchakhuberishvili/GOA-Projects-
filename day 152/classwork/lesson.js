let startTime;
let elapsedTime = 0;
let running = false;

function startStopwatch() {
  if (running) return;
  startTime = Date.now() - elapsedTime;
  running = true;
  setInterval(() => {
    elapsedTime = Date.now() - startTime;
    console.log((elapsedTime / 1000).toFixed(2) + " seconds");
  }, 100);
}

function stopStopwatch() {
  running = false;
  console.log("Stopped at: " + (elapsedTime / 1000).toFixed(2) + " seconds");
}

startStopwatch();


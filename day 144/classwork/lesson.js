const display = document.getElementById("display");
let currentInput = "";

function updateDisplay(value) {
  display.textContent = value;
}

document.querySelectorAll(".button").forEach(button => {
  button.addEventListener("click", function() {
    const value = button.textContent;
    if (value === "=") {
      currentInput = eval(currentInput);
      updateDisplay(currentInput);
    } else if (value === "C") {
      currentInput = "";
      updateDisplay(currentInput);
    } else {
      currentInput += value;
      updateDisplay(currentInput);
    }
  });
});

const rollButton = document.getElementById("rollButton");
const resultDisplay = document.getElementById("result");

rollButton.addEventListener("click", function() {
  const roll = Math.floor(Math.random() * 6) + 1;
  resultDisplay.textContent = `You rolled: ${roll}`;
});

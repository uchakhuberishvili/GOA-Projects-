const passwordInput = document.getElementById("password");
const strengthDisplay = document.getElementById("strength");

passwordInput.addEventListener("input", function() {
  const password = passwordInput.value;
  let strength = "Weak";
  if (password.length > 8) strength = "Moderate";
  if (password.match(/[A-Z]/) && password.match(/\d/)) strength = "Strong";
  strengthDisplay.textContent = strength;
});

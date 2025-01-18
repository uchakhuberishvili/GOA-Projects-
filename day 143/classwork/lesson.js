const addButton = document.getElementById("addButton");
const inputField = document.getElementById("inputField");
const list = document.getElementById("list");

addButton.addEventListener("click", function() {
  const li = document.createElement("li");
  li.textContent = inputField.value;
  list.appendChild(li);
  inputField.value = "";
});

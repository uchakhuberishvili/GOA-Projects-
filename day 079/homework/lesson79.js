const passwordInput = document.getElementById('password');
const validationMessage = document.getElementById('message');
const forms = document.getElementById('forms');
const clearButton = document.getElementById('clear');
const aboutMeInput = document.getElementById('me');
const meCounter = document.getElementById('me-counter');
const maxLength = 200;
const colorSelect = document.getElementById('color-select');
const colorDisplay = document.getElementById('color-display');

passwordInput.addEventListener('input', function() {
  const passwordLength = passwordInput.value.length;
  if (passwordLength === 0) {
    validationMessage.textContent = '';
  } else if (passwordLength < 8) {
    validationMessage.textContent = 'Password is too short. It should be at least 8 characters.';
  } else {
    validationMessage.textContent = 'Password length is sufficient.';
  }
});

clearButton.addEventListener('click', function() {
  forms.reset();
  validationMessage.textContent = ''; 
  meCounter.textContent = `0/${maxLength} characters`; 
  colorDisplay.textContent = 'Selected color will be displayed here';
});

aboutMeInput.addEventListener('input', function() {
  const currentLength = aboutMeInput.value.length;
  meCounter.textContent = `${currentLength}/${maxLength} characters`;
  
  if (currentLength > maxLength) {
    meCounter.classList.add('warning');
  } else {
    meCounter.classList.remove('warning');
  }
});

colorSelect.addEventListener('change', function() {
  const selectedColor = colorSelect.value;
  if (selectedColor) {
    colorDisplay.textContent = `Selected color: ${selectedColor}`;
  } else {
    colorDisplay.textContent = 'Selected color will be displayed here';
  }
});

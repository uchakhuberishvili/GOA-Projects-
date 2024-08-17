// function calculate() {
//     const num1 = Number(document.getElementById('number1').value);
//     const num2 = Number(document.getElementById('number2').value);
//     const result = num1 + num2;
//     document.getElementById('result').innerText = result;
// }


function submit() {

    const form = document.querySelector('form');

    const fullnameValue = form.elements.fullname.value;
    const emailValue = form.elements.email.value;
    const passValue = form.elements.password.value;
    const colorValue = form.elements.color.value;

 
    if (fullnameValue === '' || emailValue === '' || passValue === '' || colorValue === '') {
        alert('Please fill in all fields');
        return;
    }

    console.log('Form submitted successfully');
    console.log("Full Name: " + fullnameValue);
    console.log("Email: " + emailValue);
    console.log("Password: " + passValue);
    console.log("Favorite Color: " + colorValue);
}

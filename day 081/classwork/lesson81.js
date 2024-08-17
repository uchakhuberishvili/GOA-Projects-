
let my = [];


const form = document.getElementById('forms');


form.addEventListener('submit', function(event) {
    event.preventDefault();


    const firstName = document.getElementById('firstname').value;
    const lastName = document.getElementById('lastname').value;
    const email = document.getElementById('gmail').value;

    const newUser = {
        firstName: firstName,
        lastName: lastName,
        email: email
    };


    my.push(newUser);

    form.reset();

    console.log(my);
});






// const form = document.getElementById('myForm');
// const btn = document.getElementById('btn');

// const dataBase = [];

// function validateForm() {
//     const emailValue = form.elements.email.value;
//     const passValue = form.elements.password.value;

//     if(emailValue == '' || passValue == '') {
//         alert('Please fill in all fields');
//         return;
//     } 

//     const acc = {
//         email: emailValue,
//         password: passValue
//     }

//     dataBase.push(acc);

//     console.log(dataBase)

// }


// btn.onclick = validateForm;

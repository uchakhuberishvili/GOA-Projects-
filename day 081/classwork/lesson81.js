
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








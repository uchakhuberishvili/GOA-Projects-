let database = [];

function account(firstName, lastName, email) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.email = email;
}

document.getElementById('forms').addEventListener('submit', function(event) {
    event.preventDefault(); 
    let firstName = document.getElementById('firstname').value;
    let lastName = document.getElementById('lastname').value;
    let email = document.getElementById('email').value;


    let newaccount = new account(firstName, lastName, email);


    database.push(newaccount);

    console.log('registration completed succesfully!', database);
});


// const form = document.getElementById('myForm');

// const database = [];

// function Account(firstname, lastname, email){
//     this.firstname = firstname;
//     this.lastname = lastname;
//     this.email = email;
// }

// form.addEventListener("submit", function(e){
//     e.preventDefault();

//     const firstname = form.firstname.value;
//     const lastname = form.lastname.value;
//     const email = form.email.value;

//     const acc = new Account(firstname, lastname, email);

//     database.push(acc);

//     console.log(database);
// })
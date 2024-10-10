
class Account {
    constructor(firstName, lastName, email, password, city) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.password = password;
        this.city = city;
    }


    printDetails() {
        return `სახელი: ${this.firstName}, გვარი: ${this.lastName}, იმეილი: ${this.email}, ქალაქი: ${this.city}`;
    }
}


const accounts = [];


document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();


    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const city = document.getElementById('city').value;


    const newAccount = new Account(firstName, lastName, email, password, city);


    accounts.push(newAccount);


    updateAccountsList();
});


function updateAccountsList() {
    const accountsList = document.getElementById('accountsList');
    accountsList.innerHTML = '';

    accounts.forEach((account, index) => {
        const listItem = document.createElement('li');
        listItem.textContent = account.printDetails();
        accountsList.appendChild(listItem);
    });
}

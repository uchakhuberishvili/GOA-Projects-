class Car {
    constructor(make, model) {
        this.make = make;
        this.model = model; 
    }
}


let myCar = new Car("Toyota", "Corolla");



class BankAccount {
    #balance;

    constructor(balance = 0) {
        this.#balance = balance;
    }

    deposit(amount) {
        if (amount > 0) {
            this.#balance += amount;
            return `Deposited: ${amount}. New Balance: ${this.#balance}`;
        }
        return "Deposit amount must be positive.";
    }

    withdraw(amount) {
        if (amount > 0 && amount <= this.#balance) {
            this.#balance -= amount;
            return `Withdrawn: ${amount}. New Balance: ${this.#balance}`;
        }
        return "Insufficient balance or invalid amount.";
    }
}


let account = new BankAccount(100);




class MathOperations {
    static PI = 3.14159;  

    static add(a, b) {
        return a + b;  
    }
}


class User {
    #validatePassword(password) {
        return password.length >= 8;
    }

    setPassword(password) {
        if (this.#validatePassword(password)) {
            this.password = password;
            console.log("Password set successfully.");
        } else {
            console.log("Password is too weak.");
        }
    }
}


let user = new User();
user.setPassword("strongPass");
user.setPassword("weak");

class Student {
    constructor(name, grade) {
        this.name = name;
        this.grade = grade;
    }

    static compareGrades(student1, student2) {
        if (student1.grade > student2.grade) {
            return `${student1.name} has a higher grade.`;
        } else if (student1.grade < student2.grade) {
            return `${student2.name} has a higher grade.`;
        } else {
            return "Both students have the same grade.";
        }
    }
}
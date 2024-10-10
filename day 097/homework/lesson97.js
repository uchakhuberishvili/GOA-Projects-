class Person {
    constructor(name, city) {
        this.name = name;
        this.city = city;
    }

    showInfo() {
        console.log(`${this.name} lives in ${this.city}`);
    }
}

const people = [];

function createPerson(name, city) {
    const person = new Person(name, city);
    people.push(person);
}

createPerson('ucha', 'georgia');
people[0].showInfo();

class Animal {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    speak() {
        console.log(`${this.name} makes a sound`);
    }
}

class Dog extends Animal {
    speak() {
        console.log(`${this.name} says: ვაფ ვაფ!`);
    }
}

class Cat extends Animal {
    speak() {
        console.log(`${this.name} says: მიაუ!`);
    }
}

class Vehicle {
    constructor(make, model) {
        this.make = make;
        this.model = model;
    }

    displayInfo() {
        console.log(`Make: ${this.make}`);
        console.log(`Model: ${this.model}`);
    }
}

class Car extends Vehicle {
    constructor(make, model, fuelType) {
        super(make, model);
        this.fuelType = fuelType;
    }
    displayInfo() {
        super.displayInfo();
        console.log(`Fuel Type: ${this.fuelType}`);
    }
}



class Shape {
    constructor(name, sides) {
        this.name = name;
        this.sides = sides;
    }


    displayInfo() {
        console.log(`Shape: ${this.name}`);
        console.log(`Sides: ${this.sides}`);
    }
}


class Triangle extends Shape {
    constructor(base, height) {
        super('Triangle', 3);
        this.base = base;
        this.height = height;
    }

    calculateArea() {
        return (this.base * this.height) / 2;
    }
}

let students = new Map();

products.set("ucha", 100);
console.log("student 'ucha' has joined.");
    
products.set("jorgi", 10);
console.log("student 'jorgi' has joined.");
    
products.set("idk", 50);
console.log("Product 'idk' has been added.");
    
let score = students.get("jorgi");
console.log(`The score of student is: $${score}`);

let movies = new Map();
movies.set("prison break", 2002);
movies.set("dexter", 2000);
movies.set("snowfall", 2018);

if (movies.has("prison break")) {
    console.log("The movie 'prison break' is in the list.");
} else {
    console.log("The movie 'prison break' is not in the list.");
}



let actors = new Map();
actors.set("michael scofield");
actors.set("lincoln burrows");
actors.set("tbag");

actors.delete("tbag");
console.log("tbag has been removed.");



let cars = new Map();
cars.set("Toyota", "Camry");
cars.set("lamborgini", "huracan");
cars.set("Audi", "Ar8");

cars.clear();
console.log("All cars have been removed.");

if (cars.size === 0) {
    console.log("The car list is now empty.");
}

let countries = new Map();
countries.set("US", "United States");
countries.set("GE", "Georgia");
countries.set("FR", "France");

for (let code of countries.keys()) {
    console.log(`Country code: ${code}`);
}

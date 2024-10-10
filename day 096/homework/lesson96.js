const person = {
    name: 'ucha khuberishvili',
    age: 15,
    city: 'mtskheta'
}
console.log(person)

console.log(person.name)

console.log(person.city)

const { name, age } = person;

console.log(name);

console.log(age);

const student = {
    name: "giorgi",
    age: 12,
    address: {
        city: "tbilisi",
        country: "georgia"
    }
};

const { address: { city, country } } = student;

console.log(city);

console.log(country);

const product = {
    name: "Laptop",
    price: 1200
};


const { names, category = "general" } = product;

console.log(name);

console.log(category);

const user = { name: "luka", age: 29 };

const locations = { city: "mtskheta", country: "georgia" };


const merged = { ...user, ...location };

console.log(merged);

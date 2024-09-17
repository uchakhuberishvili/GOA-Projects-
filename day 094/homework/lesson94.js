const cars = ["mersedes", "bmw", "audi", "bentley", "toyota"];

cars.forEach(Element => {console.log(Element);});

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const newArray = numbers.map(Number => Number * 123);

console.log(newArray);

const result = numbers.filter(number => number > 3);

console.log(result);

const nums = [2,3,4,5];

const reducer = (accumulator, currentValue) => accumulator + currentValue;


const sum = numbers.reduce(reducer);

const sunWithInitialValue = numbers.reduce(reducer, 1);

console.log(sum);

console.log(sunWithInitialValue);


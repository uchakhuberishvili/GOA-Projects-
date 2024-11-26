const { calculate, filter } = require('./calculator');

console.log(calculate(10, 5, '+'));
console.log(calculate(20, 10, '*'));

const numbers = [1, 2, 3, 4, 5];
const isEven = (num) => num % 2 === 0;
console.log(filter(numbers, isEven));

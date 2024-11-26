const multiply = (a) => (b) => (c) => a * b * c;

const result = multiply(2)(3)(4);
console.log(result);

function createCounter() {
    let count = 0;
    return () => ++count;
}

const counter = createCounter();
console.log(counter());
console.log(counter());

const key = "color";
const value = "blue";

const obj = { [key]: value };
console.log(obj);
const set = new Set([1, 2, 3, 2]);
const map = new Map([["name", "Alice"], ["age", 25]]);

console.log(set);
console.log(map.get("name"));

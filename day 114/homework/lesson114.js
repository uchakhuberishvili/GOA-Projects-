//testing node

console.log("Hello, Node.js!");
console.log("Sum of 2 + 3 is:", 2 + 3);
console.warn("This is a warning message!");
console.error("This is an error message!");


const name = "Node";
const version = "23";
console.log(`Hello, ${name}! Running on version ${version}.`);

function greet(name) {
    return `Hello, ${name}!`;
}

console.log(greet("Node.js"));
console.log(greet("Developer"));

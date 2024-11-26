const user = {
    name: "Alice",
    age: 25,
    greet() {
        return `Hello, ${this.name}`;
    },
};

const { name, greet } = user;
console.log(name);
console.log(greet());

const fetchData = () =>
    new Promise((resolve, reject) => {
        setTimeout(() => resolve("Data loaded"), 2000);
    });

async function loadData() {
    const data = await fetchData();
    console.log(data);
}

loadData();
function applyOperation(arr, operation) {
    return arr.map(operation);
}

const numbers = [1, 2, 3, 4];
const doubled = applyOperation(numbers, (n) => n * 2);
console.log(doubled);

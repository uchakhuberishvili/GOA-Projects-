function calculate(a, b, operation) {
    if (operation === '+') return a + b;
    if (operation === '-') return a - b;
    if (operation === '*') return a * b;
    if (operation === '/') return b !== 0 ? a / b : 'Cannot divide by zero';
    return 'Invalid operation';
}

function filter(array, func) {
    const result = [];
    for (let i = 0; i < array.length; i++) {
        if (func(array[i])) {
            result.push(array[i]);
        }
    }
    return result;
}

module.exports = { calculate, filter };

function greet(name) {
    console.log(`Hello, ${name}!`);
}

function calculateAverage(numbers) {
    let sum = 0;
    for(let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }
    return sum / numbers.length;
}

module.exports = { greet, calculateAverage };

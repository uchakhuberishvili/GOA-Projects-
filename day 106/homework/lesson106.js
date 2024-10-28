

const sumOfDivisors = (n) => {
    let sum = 0;
    for (let i = 1; i <= n; i++) {
        if (n % i === 0) {
            sum += i;
        }
    }
    return sum;
};

const perfectNumber = (n) => {
    const sum = sumOfDivisors(n);
    return n === sum && sum > 1;
};

const isPerfectSquare = (n) => {
    return Math.sqrt(n) % 1 === 0;
};

const findNthPerfectSquare = (n) => {
    let count = 0;
    let num = 1;
    while (count < n) {
        num++;
        if (isPerfectSquare(num) && perfectNumber(num)) {
            count++;
        }
    }
    return num;
};

console.log(findNthPerfectSquare(1));
function longestWordLength(str) {
    return str.split(' ')
              .reduce((max, word) => Math.max(max, word.length), 0);
}

console.log(longestWordLength("The quick brown fox jumped over the lazy dog"));

function digitalRoot(num) {
    while (num >= 10) {
        num = num.toString().split('').reduce((sum, digit) => sum + +digit, 0);
    }
    return num;
}

console.log(digitalRoot(942));


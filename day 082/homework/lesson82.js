function iteration(start, end) {
    let list = [];
    
    for (let i = start; i <= end; i++) {
        list.push(i);
    }
    
    return list;
}

let result = iteration(20, 75);
console.log(result);

function average(result) {
    let sum = 0;
    for(let i = 0; i < result.length; i++) {
        sum += result[i];
    }
    return sum / result.length;
}

let totalSum = average(result);
console.log(totalSum);


for (let i = 0; i < 5; i++) {
    console.log(i);
}

for (let i = 10; i >= 1; i--) {
    console.log(i);
}

for (let i = 1; i <= 5; i++) {
    console.log(i * i);
}


let names = ['ucha', 'gio', 'data'];
for (let i = 0; i < names.length; i++) {
    console.log(names[i]);
}
let sum = 0;
for (let i = 1; i <= 50; i++) {
    sum += i;
}
console.log(sum);

let i = 1;
do {
    console.log(i * i);
    i++;
} while (i <= 5);

let is = 1;
let sums = 0;
do {
    sum += is;
    is++;
} while (is <= 5);
console.log(sums);


let ios = 0;
do {
    console.log(ios);
    ios += 2;
} while (ios <= 10);


let ias = 100;
do {
    console.log(ias);
    ias--;
} while (ias >= 1);



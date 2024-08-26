function manual_second(num) {
    return num % 2 === 0;
}

function manualFilter(manual_second, Array) {
    let result = [];

    for (let i = 0; i < Array.length; i++) {
        if (manual_second(Array[i])) {
            result.push(Array[i]);
        }
    }

    return result;
}

let nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];
let filteredArray = manualFilter(manual_second, nums);
console.log(filteredArray);

// ქოდვარსები ავტვირთე CodeWars ფოლდერში სულ მაღლა სახელად "day 084 codewars"
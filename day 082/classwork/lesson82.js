function evenSum(border) {
    let sum = 0;
    for(let i = 0;border >= i; i++) {
        if (i % 2 === 0){
            sum += i;
        }
    }
    return sum
}
console.log(evenSum(20))



for(let i = 20;i != -1; i--) {
    console.log(i)
}



for (let i = 0; i != 10; i+2) {
    console.log(i);
}



function generateEven(border) {
    let list = [];
    for (let i = 0; i <= border; i++) {
        if (i % 2 === 0) {
            list.push(i);
        }
    }
    return list;
}



let nums = generateEven(10);
console.log(nums);

let result = 0;
for (let i = 0; i < nums.length; i++) {
    console.log(nums[i]); 
    result += nums[i]; 
}



console.log(result);



const numbers = [1, 2, 3, 4, 5];

for(let i = 0; i < nums.length; i++) {
    console.log(nums[i]);
}



for(let i = 0; i != 10; i++) {
    let value = i;
    let result = "none";
    
    if (i % 2 === 0) {
        result = "even";
    } else {
        result = "uneven";
    }
    let type = result;
    console.log(`Value: ${value}, Type: ${type}`);
}



const numsType = [];

for(let i = 0; i < 10; i++) {
    const numType = {
        value: i,
        type: ''
    }
    if(i % 2 === 0) {
        numType.type = 'Even';
    } else {
        numType.type = 'Odd';
    }

    numsType.push(numType);
}



console.log(numsType);


let pass;
let tryes= 3; 

while (pass !== "sitepass" && tryes > 0) {
    pass = prompt(`Enter The Password (${tryes} attempts left):`);
    
    if (pass === "sitepass") {
        alert("Access Granted!");
        break;
    } else {
        tryes--; 
        if (tryes> 0) {
            alert("Incorrect password. Try again.");
        } else {
            alert("Access Denied. No attempts left.");
        }
    }
}



let authorized = false;
let count = 3;

while (authorized !== true && count > 0) {
    const pass = prompt("Enter your password:");
    
    if (pass === "luka") {
        authorized = true;
        alert("Access granted!");
    } else {
        count--;
        alert("Access denied. You have " + count + " attempts left.");
    }
}



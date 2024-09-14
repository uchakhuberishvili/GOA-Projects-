// Math object methods in javascript

// Math.round - rounds to closest integer 
// Math.floor - rounds down to closest integer
// Math.celi -  rounds number up regardless of decimal point
// Math.trunc - removes decimal part of intger
// Math.pow - squares integer
// Math.sqrt - takes square root from number
// Math.cbrt - takes cube root from number
// Math.min - returns minimal number
// Math.max - returns maximal number
// Math.random - returns random number in 0,1 range

// Date constructor arguments in javascript

// new Date(year,month,time)

// date.toString() - converts time to human readable format
// date.DateString() - short readable format
// date.to(Timezone)String - converts time to specific timezone

// getFullYear - Get year as four digit number
// getMonth - Get month in nth format
// getDay - Get weekday in nth format
// getDate - Gets day of month
// getHours - Gets hours

// let time = 10;
// const id = setInterval(function{
//     time --;
//     console.log(time)
//     if(time === 0){
//         clearInterval(id);
//     }
//     console.log(id);
// },1000)



let time = 0;

let date = setInterval(function() {
    time++;
    console.log(time);

    if (time === 35) {
        console.log("Time hit 35 seconds");
        clearInterval(date);
    }
}, 1000)


let heading = document.getElementById('head');
let paragraph = document.getElementById('par');
let button = document.getElementById('but');

console.log(heading.parentElement);

console.log(heading.parentElement.children);

console.log(heading.parentElement.firstElementChild);

console.log(heading.parentElement.lastElementChild);

console.log(paragraph.previousElementSibling);

console.log(heading.nextElementSibling);

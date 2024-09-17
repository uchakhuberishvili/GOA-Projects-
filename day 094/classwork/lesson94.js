// const form = document.querySelector('form');
// const ul = document.getElementById('items');

// let index = 0;

// form.addEventListener('submit', (e) => {
//     e.preventDefault();

//     const item = form.item.value;
//     ul.innerHTML += `<li id=${index}>${item}</li>`;
//     index++;

//     form.item.value = '';

// })

// ul.addEventListener('click', (e) => {
//     if (e.target.tagName === 'LI') {
//         e.target.remove();
//     }

// შექმენით მასივი სადაც გექნებათ მინიმუმ 5 სახელი, გამოიყენეთ map მეთოდი და შეამოწმეთ შემდეგი პირობა, თუ ინდექსი არის ლუწი მაშინ ახალ მასივში სახელი დაამატეთ დიდი ასოებით სხვა შემთხვევაში თუ კენტია დაამატეთ პატარა ასოებით, როცა ამას დაასრულებთ შექმენით  map მეთოდის კლონი და გააკეთეთ იგივე დავალება თვენი კლონით, აუცილებალდ ახსენით რა განსხვავებაა forEach სა და map მეთოდს შორის



let cars = ["mersedes", "bmw", "audi", "bentley", "toyota"];

let even = [];
let odd = [];

const carMap = cars.map((car, index) => {
  if (index % 2 === 0) {
    even.push(car.toUpperCase());
  } else {
    odd.push(car.toLowerCase());
  }
});

console.log("Even:", even);
console.log("Odd:", odd);
// const names = ["ucha", "nika", "luka"];

// const manualForEach = (arr, func) => {
//     for(let i = 0; i < arr.length; i++){
//         func(arr[i], i, arr)
//     }
// }

// manualForEach(names, (value) => {
//     console.log(value)
// })


// const names = ["Luka", "Lile", "Nia"];

// const newNames = names.map((curName, index, arr) => {
//     return curName + ")fwefwef"
// })


// const manualMap = (arr, func) => {
//     const result = [];
    
//     for(let i = 0; i < arr.length; i++){
//         const value = func(arr[i], i, arr);
//         result.push(value)
//     }
    
//     return result;
// }

// console.log(manualMap(names, (curValue, index) => curValue + index))


const people = [
    { name: "ucha", age: 7 },
    { name: "Luka", age: 34 },
    { name: "nika", age: 2 },
    { name: "Giorgi", age: 19 },
    { name: "data", age: 89 }
];



const underage = people.filter(person => person.age < 18);
const aboveage = people.filter(person => person.age >= 18);

console.log(underage);

console.log(aboveage);


// const names = ["Luka", "ucha", "gorila", "wafli"];

// const newNames = names.filter((curValue) => {
//     return curValue.length >= 4
// })

// console.log(newNames)

// const manualFilter = (arr, func) => {
//     const result = [];
    
//     for(let i = 0; i < arr.length; i++){
//         const bool = func(arr[i], i, arr);
        
//         if(bool) {
//             result.push(arr[i])
//         }
//     }
    
//     return result;
// }

// console.log(manualFilter(names, (curValue) => {
//     return curValue[0] != "L"
// }))

//1
let nums = [2,6,232,123,53,34,2];

const doubled = nums.map(number => number * 2)

console.log(doubled)


//2
let Even = [2,6,232,123,53,33,21];

const evenOnly = Even.filter(number => number % 2 === 0)

console.log(evenOnly)

//3
let toSquare = [2,6,232,123,53,34,2];

const square = nums.map(number => number * number)

console.log(square)


//4
let names = ["ucha", "constantine", "giorgi", "luka","alexsandre","data"]

const fiveCharacterNames = names.filter(name => name.length > 5)

console.log(fiveCharacterNames)

//5
let fruits = ["apple", "banana", "orange", "pomegrante", "cherry"]

// const capitaliFirstCharacter = fruits.map(fruit =>)
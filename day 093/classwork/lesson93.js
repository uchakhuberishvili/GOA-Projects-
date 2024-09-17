//თუ ვარ შექმნილია ფუნქციის შიგნით ის მხოლოდ ფუნქციაში იქნება ხელმისაწვდომი,თუ შევქმნით ფუნქციის გარეთ, მაშინ იქნება გლობალური

//ჰოისტინგი არის როდესაც შეგვიძლია ცვლადი გამოვიყენოთ სანამ იგი შეიქმნება მაგრამ ის იქნება undefined.

//ლოკალური ნისნავს რომ იგი მხოლოდ იქ გამოიყენება რომელ ფუნქციაშიც შეიქმნა,და მხოლოდ მანდ გამოიყენება,სხხვაგან არა


function firstlesson() {
    console.log(num);
    var num = 7;
    console.log(num);
}

firstlesson();

function secondlesson() {
    //console.log(num);
    let num = 6;
    console.log(num);
}

secondlesson();

function thirdLesson() {
    //console.log(num);
    const num = 5;
    console.log(num);
}

thirdLesson();

//ცვლადები ჰოისტინგდება სუფთამდე. ეს ნიშნავს, რომ ცვლადი შეიძლება გამოვიყენოთ სანამ მისი დეკლარაცია მოხდება, მაგრამ ის იქნება undefined სანამ დეკლარაცია არ შეისწავლის.

//var არის ფუნქციის სუფთა. ეს ნიშნავს, რომ თუ var დეკლარირებულია ფუნქციის შიგნით, ის მხოლოდ იმ ფუნქციაში იქნება ხელმისაწვდომი. თუ დეკლარირებულია ფუნქციის გარეთ, ეს გლობალურად არის ხელმისაწვდომი.


const cube = (num) => num * num;
console.log(cube(5));

const sum = (a,b) => a + b;
console.log(sum(5,24));

const learning = (language) => "learning " + language;
console.log(learning("JavaScript"));


//const OddEven = (num) => num % 2 === 0;
//console.log(OddEven(5)); 

// const me = (name, age) => ${name} ${age};
// console.log(me("ucha", 15));

const first = (a,b) => {
    const second = (c,d) => c + d;
    return second(a,b);
}
console.log(first(2,6))
const cars = ["mersedes","bwm","lamborgini","porshe","toyota"]
cars.push("bentley") // დაამატებს სიის ბოლოში სტრინგს(bentley)
cars.push("volkswagen")// დაამატებს სიის ბოლოში სტრინგს(volkswagen)
cars.unshift("jiguli")// დაამატებს სიის დასაწყისში სტრინგს(jiguli)
cars.unshift("ford")// დაამატებს სიის დასაწყისში სტრინგს(ford)
cars.shift()// შლის სიის დასაწყისში სტრინგს(ford)
cars.unshift("audi")// დაამატებს სიის ბოლოში სტრინგს(audi)
console.log(cars)


const car = ["mersedes", "bwm", "lamborgini", "mersedes", "mersedes", "lamborgini", "porshe", "audi", "porshe", "bwm", "porshe", "audi"];

let carTypes = {
    indexOne: car.indexOf("lamborgini"), // პოულობს "lamborgini"-ს პირველი ინდექს
    indexTwo: car.indexOf("mersedes"), // პოულობს "mersedes"-ს პირველი ინდექს
    indexThree: car.lastIndexOf("mersedes"), // პოულობს "mersedes"-ს ბოლო ინდექს
    indexFour: car.lastIndexOf("audi"), // პოულობს "audi"-ს ბოლო ინდექს
    indexFive: car.lastIndexOf("porshe"), // პოულობს "porshe"-ს ბოლო ინდექს
    indexSix: car.includes("jiguli"), // აბრუნებს boolean-ს, არის თუ არა "jiguli" მასივში (False)
    indexSeven: car.includes("bwm") // აბრუნებს boolean-ს, არის თუ არა "bwm" მასივში (True)
};

console.log(carTypes);
const fruits = ["ვაშლი", "ბროწეული", "ბანანი", "ალუჩა"];
sorted = fruits.sort();
console.log(sorted)


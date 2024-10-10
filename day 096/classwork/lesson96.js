// const numbers = [1,2,3,4,5];

// const sum = numbers.reduce((acc, cur) => {
//     return acc + cur
// }, 10);




// const manualReduce = (arr, func, startingValue = 0) => {
//     let acc = startingValue;

//     for(const value of arr){
//         acc = func(acc, value);
//     }

//     return acc;
// }

// console.log(manualReduce(numbers, (acc, cur) => acc + cur, 10))

const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10];

let evenOdd = numbers.map((number, index) => {
    if (index % 2 === 0) {
      return number * 2;
    } else {
      return number;
    }
  });
console.log(evenOdd);

function clone(nums) {
    let clone = []; // შევქნათ ცარიელი მასივი
  
    for (let i = 0; i < nums.length; i++) {
      if (i % 2 === 0) {
        clone.push(nums[i] * 2); // თუ ინდექსი ლუწია, ამრავლებს 2-ზე და ამატებს clone მასივში
      } else {
        clone.push(nums[i]);// თუ ინდექსი კენტია, უბრალოდ ამატებს clone მასივში
      }
    }
  
    return clone;
  }
  
  console.log(clone([12,3221,32,123,42,23,11,2112,22,33,42]));


//   const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

// const evenNumbers = numbers.filter(number => number % 2 === 0);


// const manualFilter = (arr, func) => {
//     const result = [];

//     for(let i = 0; i < arr.length; i++){
//         if(func(arr[i], i, arr)){
//             result.push(arr[i]);
//         }
//     }

//     return result;
// }
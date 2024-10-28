const promise1 = new Promise((resolve) => resolve("Hello, Promise!"));
promise1.then(console.log);

const promise2 = new Promise((_, reject) => reject("Something went wrong!"));
promise2.catch(console.error);

const promise3 = new Promise((resolve) => {
    setTimeout(() => resolve("2 seconds have passed"), 2000);
});
promise3.then(console.log);

const promise4 = new Promise((resolve, reject) => {
    Math.random() > 0.5 ? resolve("Success!") : reject("Failed!");
});
promise4.then(console.log).catch(console.error);

const promise5 = new Promise((resolve) => resolve(5));
promise5
    .then((num) => num * 2)
    .then((num) => num * 2)
    .then((num) => num * 2)
    .then(console.log);

    
const promise6 = new Promise((resolve) => {
    setTimeout(() => resolve("Data fetched!"), 1000);
});
promise6.then(console.log);

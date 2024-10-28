

function eventLoopFunction1() {
  console.log('Function 1');
  setTimeout(eventLoopFunction2, 0);
}

function eventLoopFunction2() {
  console.log('Function 2');
  setTimeout(eventLoopFunction3, 0);
}

function eventLoopFunction3() {
  console.log('Function 3');
}


eventLoopFunction1();



setTimeout(() => {
  console.log('Delay');
}, 0);



console.log('Other JavaScript code');



setTimeout(() => {
  console.log('Timer');
}, 100);



new Promise((resolve) => {
  console.log('Promise');
  resolve();
}).then(() => {
  console.log('Promise resolved');
});



function callbackFunction(data) {
  console.log('Callback', data);
}

setTimeout(() => {
  callbackFunction('Callback data');
}, 500);
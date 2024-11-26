function debounce(func, delay) {
    let timer;
    return function (...args) {
        clearTimeout(timer);
        timer = setTimeout(() => func.apply(this, args), delay);
    };
}

const log = debounce((message) => console.log(message), 1000);

log("First call");
log("Second call");

function throttle(func, limit) {
    let lastCall = 0;
    return function (...args) {
        const now = Date.now();
        if (now - lastCall >= limit) {
            lastCall = now;
            func.apply(this, args);
        }
    };
}

const throttledLog = throttle((message) => console.log(message), 1000);

throttledLog("Call 1");
throttledLog("Call 2");

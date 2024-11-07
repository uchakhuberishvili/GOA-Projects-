const http = require('http');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello, World!\n');
});

const port = 3000;
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});


const http = require('http');

const servers = http.createServer((req, res) => {
    if (req.url === '/') {
        res.end('Home Page');
    } else if (req.url === '/about') {
        res.end('About Page');
    } else {
        res.statusCode = 404;
        res.end('404 Not Found');
    }
});

server.listen(3000, () => {
    console.log("Server listening on http://localhost:3000");
});


const EventEmitter = require('events');
const eventEmitter = new EventEmitter();

eventEmitter.on('greet', (name) => {
    console.log(`Hello, ${name}!`);
});

eventEmitter.emit('greet', 'Node.js');
eventEmitter.emit('greet', 'Developer');


const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

rl.question("What's your name? ", (name) => {
    console.log(`Hello, ${name}!`);
    rl.close();
});


const { exec } = require('child_process');

exec('ls', (error, stdout, stderr) => {
    if (error) {
        console.error(`Error executing command: ${error}`);
        return;
    }
    console.log(`Output:\n${stdout}`);
});


const crypto = require('crypto');

const hash = crypto.createHash('sha256').update('Hello, Node.js!').digest('hex');
console.log("SHA-256 Hash:", hash);

crypto.randomBytes(16, (err, buffer) => {
    if (err) throw err;
    console.log("Random token:", buffer.toString('hex'));
});

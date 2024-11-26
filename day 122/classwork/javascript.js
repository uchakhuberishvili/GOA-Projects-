import React from 'react';
import ReactDOM from 'react-dom';

function App() {
    return (
        <div>
            <h1>Hello, React!</h1>
            <p>Welcome to your first React app.</p>
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));

function Greeting({ name }) {
    return <h1>Hello, {name}!</h1>;
}

function App() {
    return (
        <div>
            <Greeting name="Alice" />
            <Greeting name="Bob" />
        </div>
    );
}

import React, { useState } from 'react';

function Counter() {
    const [count, setCount] = useState(0);

    return (
        <div>
            <h1>Count: {count}</h1>
            <button onClick={() => setCount(count + 1)}>Increase</button>
            <button onClick={() => setCount(count - 1)}>Decrease</button>
        </div>
    );
}

export default Counter;

function ButtonClicker() {
    const handleClick = () => {
        alert('Button was clicked!');
    };

    return <button onClick={handleClick}>Click Me</button>;
}

function ShoppingList() {
    const items = ['Apples', 'Oranges', 'Bananas'];

    return (
        <ul>
            {items.map((item, index) => (
                <li key={index}>{item}</li>
            ))}
        </ul>
    );
}

import React, { useState, useEffect } from 'react';

function UsersList() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('https://jsonplaceholder.typicode.com/users')
            .then(response => response.json())
            .then(data => setUsers(data));
    }, []);

    return (
        <ul>
            {users.map(user => (
                <li key={user.id}>{user.name}</li>
            ))}
        </ul>
    );
}

function Counter() {
    const [count, setCount] = React.useState(0);

    return (
        <div>
            <h1>Count: {count}</h1>
            <button onClick={() => setCount(count + 1)}>Increment</button>
            <button onClick={() => setCount(count - 1)}>Decrement</button>
            <button onClick={() => setCount(0)}>Reset</button>
        </div>
    );
}

ReactDOM.render(<Counter />, document.getElementById("root"));
function TodoList() {
    const [tasks, setTasks] = React.useState([]);
    const [input, setInput] = React.useState("");

    const addTask = () => {
        if (input.trim()) {
            setTasks([...tasks, input]);
            setInput("");
        }
    };

    return (
        <div>
            <h1>To-Do List</h1>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Enter a task"
            />
            <button onClick={addTask}>Add Task</button>
            <ul>
                {tasks.map((task, index) => (
                    <li key={index}>{task}</li>
                ))}
            </ul>
        </div>
    );
}

ReactDOM.render(<TodoList />, document.getElementById("root"));

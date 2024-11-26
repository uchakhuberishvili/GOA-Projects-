import React, { useState } from "react";

function TodoApp() {
    const [tasks, setTasks] = useState([]);
    const [input, setInput] = useState("");

    const addTask = () => {
        if (input.trim()) {
            setTasks([...tasks, { text: input, completed: false }]);
            setInput("");
        }
    };

    const toggleTask = (index) => {
        const updatedTasks = tasks.map((task, i) =>
            i === index ? { ...task, completed: !task.completed } : task
        );
        setTasks(updatedTasks);
    };

    const deleteTask = (index) => {
        setTasks(tasks.filter((_, i) => i !== index));
    };

    return (
        <div>
            <h1>Todo App</h1>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Enter a task"
            />
            <button onClick={addTask}>Add Task</button>
            <ul>
                {tasks.map((task, index) => (
                    <li key={index}>
                        <span
                            style={{
                                textDecoration: task.completed
                                    ? "line-through"
                                    : "none",
                            }}
                            onClick={() => toggleTask(index)}
                        >
                            {task.text}
                        </span>
                        <button onClick={() => deleteTask(index)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default TodoApp;

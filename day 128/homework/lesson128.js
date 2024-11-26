import React, { useState } from 'react';
import ReactDOM from 'react-dom';

function App() {
  const [tasks, setTasks] = useState([]);
  const [taskInput, setTaskInput] = useState('');

  const addTask = () => {
    if (taskInput.trim() === '') return;
    setTasks([...tasks, { text: taskInput, completed: false }]);
    setTaskInput('');
  };

  const toggleTaskCompletion = (index) => {
    const updatedTasks = tasks.map((task, i) =>
      i === index ? { ...task, completed: !task.completed } : task
    );
    setTasks(updatedTasks);
  };

  const removeTask = (index) => {
    const updatedTasks = tasks.filter((_, i) => i !== index);
    setTasks(updatedTasks);
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <h1>To-Do List</h1>
      <input
        type="text"
        value={taskInput}
        onChange={(e) => setTaskInput(e.target.value)}
        placeholder="Enter a task"
        style={{ padding: '8px', marginRight: '10px' }}
      />
      <button onClick={addTask} style={{ padding: '8px', cursor: 'pointer' }}>
        Add Task
      </button>
      <ul style={{ listStyleType: 'none', padding: '0' }}>
        {tasks.map((task, index) => (
          <li
            key={index}
            style={{
              padding: '10px',
              margin: '5px 0',
              backgroundColor: task.completed ? '#d3ffd3' : '#f2f2f2',
              textDecoration: task.completed ? 'line-through' : 'none',
            }}
          >
            {task.text}
            <button
              onClick={() => toggleTaskCompletion(index)}
              style={{
                marginLeft: '10px',
                padding: '5px',
                cursor: 'pointer',
              }}
            >
              {task.completed ? 'Undo' : 'Complete'}
            </button>
            <button
              onClick={() => removeTask(index)}
              style={{
                marginLeft: '10px',
                padding: '5px',
                cursor: 'pointer',
                backgroundColor: 'red',
                color: 'white',
              }}
            >
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById('root'));

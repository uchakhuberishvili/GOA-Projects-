import React, { useState } from "react";

const Todo = () => {
  const [tasks, setTasks] = useState([]);
  const [task, setTask] = useState("");
  return (
    <div>
      <input onChange={(e) => setTask(e.target.value)} value={task} />
      <button onClick={() => setTasks([...tasks, task])}>Add</button>
      <ul>{tasks.map((t, i) => <li key={i}>{t}</li>)}</ul>
    </div>
  );
};

export default Todo;

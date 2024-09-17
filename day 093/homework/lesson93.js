
const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskBtn');
const taskList = document.getElementById('taskList');
const clearAllBtn = document.getElementById('clearAllBtn');


window.addEventListener('DOMContentLoaded', loadTasks);


addTaskBtn.addEventListener('click', () => {
    const task = taskInput.value.trim();
    if (task !== '') {
        addTask(task);
        saveTasks();
        taskInput.value = '';
    }
});


clearAllBtn.addEventListener('click', () => {
    taskList.innerHTML = '';
    localStorage.removeItem('tasks');
});


const addTask = (taskText) => {
    const li = document.createElement('li');
    li.innerHTML = `
        <input type="checkbox" class="checkTask">
        <span>${taskText}</span>
        <button class="deleteTask">Delete</button>
    `;

    li.querySelector('.checkTask').addEventListener('change', (e) => {
        li.querySelector('span').classList.toggle('completed', e.target.checked);
        saveTasks();
    });


    li.querySelector('.deleteTask').addEventListener('click', () => {
        li.remove();
        saveTasks();
    });

    taskList.appendChild(li);
};


const saveTasks = () => {
    const tasks = [];
    taskList.querySelectorAll('li').forEach(li => {
        tasks.push({
            text: li.querySelector('span').textContent,
            completed: li.querySelector('.checkTask').checked
        });
    });
    localStorage.setItem('tasks', JSON.stringify(tasks));
};


const loadTasks = () => {
    const tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.forEach(task => {
        addTask(task.text);
        const taskElement = taskList.lastElementChild;
        taskElement.querySelector('.checkTask').checked = task.completed;
        taskElement.querySelector('span').classList.toggle('completed', task.completed);
    });
};

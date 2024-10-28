document.addEventListener('DOMContentLoaded', loadTodos);

function addTodo() {
    const todoInput = document.getElementById('todo-input');
    const task = todoInput.value.trim();
    if (task === '') return;
    
    const todos = getTodosFromStorage();
    todos.push({ task, completed: false });
    saveTodosToStorage(todos);
    renderTodos(todos);
    todoInput.value = '';
}

function loadTodos() {
    const todos = getTodosFromStorage();
    renderTodos(todos);
}

function renderTodos(todos) {
    const todoList = document.getElementById('todo-list');
    todoList.innerHTML = '';

    todos.forEach((todo, index) => {
        const todoItem = document.createElement('div');
        todoItem.className = 'todo-item';

        const taskText = document.createElement('span');
        taskText.textContent = todo.task;
        if (todo.completed) taskText.classList.add('completed');
        taskText.onclick = () => toggleComplete(index);
        
        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.onclick = () => deleteTodo(index);

        todoItem.appendChild(taskText);
        todoItem.appendChild(deleteBtn);
        todoList.appendChild(todoItem);
    });
}

function toggleComplete(index) {
    const todos = getTodosFromStorage();
    todos[index].completed = !todos[index].completed;
    saveTodosToStorage(todos);
    renderTodos(todos);
}

function deleteTodo(index) {
    const todos = getTodosFromStorage();
    todos.splice(index, 1);
    saveTodosToStorage(todos);
    renderTodos(todos);
}

function getTodosFromStorage() {
    const todos = localStorage.getItem('todos');
    return todos ? JSON.parse(todos) : [];
}

function saveTodosToStorage(todos) {
    localStorage.setItem('todos', JSON.stringify(todos));
}

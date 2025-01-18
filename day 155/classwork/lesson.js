let todos = [];

function addTodoWithCompletion(todo) {
  todos.push({ text: todo, completed: false });
}

function toggleCompletion(todoText) {
  const todo = todos.find(t => t.text === todoText);
  if (todo) {
    todo.completed = !todo.completed;
    console.log(`${todoText} is now ${todo.completed ? 'completed' : 'not completed'}`);
  }
}

function viewTodos() {
  console.log(todos);
}

addTodoWithCompletion("Learn JavaScript");
addTodoWithCompletion("Read a book");
toggleCompletion("Learn JavaScript");
viewTodos();

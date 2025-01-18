let todoList = [];

function addTodo(todo) {
  todoList.push(todo);
  console.log(`Added: ${todo}`);
}

function removeTodo(todo) {
  const index = todoList.indexOf(todo);
  if (index > -1) {
    todoList.splice(index, 1);
    console.log(`Removed: ${todo}`);
  } else {
    console.log(`Todo not found: ${todo}`);
  }
}

function viewTodos() {
  console.log("To-Do List:", todoList);
}

addTodo("Buy groceries");
addTodo("Read a book");
viewTodos();
removeTodo("Read a book");
viewTodos();

// vite დავაინსტალირეთ

import React, { useState } from "react";
import ReactDOM from "react-dom/client";

const App = () => {
  const [users, setUsers] = useState(["Ana", "Nika", "Lasha"]);
  const [newUser, setNewUser] = useState("");

  const addUser = () => {
    if (newUser.trim() !== "") {
      setUsers([...users, newUser]);
      setNewUser("");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>User List</h1>
      <ul>
        {users.map((user, index) => (
          <li key={index}>{user}</li>
        ))}
      </ul>
      <input
        type="text"
        value={newUser}
        onChange={(e) => setNewUser(e.target.value)}
        placeholder="Enter new user"
        style={{ padding: "5px", marginRight: "10px" }}
      />
      <button onClick={addUser} style={{ padding: "5px 10px" }}>
        Add User
      </button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);

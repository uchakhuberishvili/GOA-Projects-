import { useEffect, useState } from "react";
import "./styles.css";

export default function App() {
  const [students, setStudents] = useState([]);
  const [accounts, setAccounts] = useState([]);
  const [account, setAccount] = useState(null);
  const [isEditing, setIsEditing] = useState(false);
  const [editingIndex, setEditingIndex] = useState(null);
  const [editedStudent, setEditedStudent] = useState({
    name: "",
    lastname: "",
    age: "",
  });
  useEffect(() => {
    localStorage.setItem("account", JSON.stringify(account));
    localStorage.setItem("accounts", JSON.stringify(accounts));
    localStorage.setItem("students", JSON.stringify(students));
  }, [account, accounts, students]);

  useEffect(() => {
    setStudents(JSON.parse(localStorage.getItem("students")) || []);
    setAccounts(JSON.parse(localStorage.getItem("accounts")) || []);
    setAccount(JSON.parse(localStorage.getItem("account")) || null);
  }, []);

  const handleRegister = (e) => {
    e.preventDefault();
    const newAccount = {
      email: e.target.email.value,
      pass: e.target.pass.value,
    };
    if (accounts.some((acc) => acc.email === newAccount.email)) {
      alert("Account already exists. Please log in.");
      return;
    }
    setAccounts([...accounts, newAccount]);
    alert("Account created successfully!");
    e.target.reset();
  };

  const handleSignin = (e) => {
    e.preventDefault();
    const enteredAccount = {
      email: e.target.email.value,
      pass: e.target.pass.value,
    };
    const loggedInUser = accounts.find(
      (acc) => acc.email === enteredAccount.email && acc.pass === enteredAccount.pass
    );
    if (!loggedInUser) {
      alert("Invalid credentials. Please try again.");
      return;
    }
    setAccount(loggedInUser);
    alert("Logged in successfully!");
    e.target.reset();
  };

  const logout = () => {
    setAccount(null);
    setIsEditing(false);
    setEditingIndex(null);
    setEditedStudent({ name: "", lastname: "", age: "" });
    alert("Logged out successfully!");
  };

  const addStudent = (e) => {
    e.preventDefault();
    const student = {
      name: e.target.studentName.value,
      lastname: e.target.studentLastname.value,
      age: e.target.studentAge.value,
    };
    setStudents([...students, student]);
    e.target.reset();
  };

  const deleteStudent = (index) => {
    const filteredStudents = students.filter((_, i) => i !== index);
    setStudents(filteredStudents);
    setIsEditing(false);
    setEditingIndex(null);
    setEditedStudent({ name: "", lastname: "", age: "" });
  };

  const editStudent = (index) => {
    setIsEditing(true);
    setEditingIndex(index);
    setEditedStudent({
      name: students[index].name,
      lastname: students[index].lastname,
      age: students[index].age,
    });
  };

  const handleEditChange = (e) => {
    setEditedStudent({ ...editedStudent, [e.target.name]: e.target.value });
  };

  const handleUpdateStudent = () => {
    const updatedStudents = [...students];
    updatedStudents[editingIndex] = {
      name: editedStudent.name,
      lastname: editedStudent.lastname,
      age: editedStudent.age,
    };
    setStudents(updatedStudents);
    setIsEditing(false);
    setEditingIndex(null);
    setEditedStudent({ name: "", lastname: "", age: "" });
  };
    const handleEditAccount = (e) => {
        e.preventDefault();
        const updatedAccount = {
            email: e.target.email.value,
            pass: e.target.pass.value,
        };
        const updatedAccounts = [...accounts];
        const accountIndex = updatedAccounts.findIndex((acc) => acc.email === account.email);
        if (accountIndex !== -1) {
            updatedAccounts[accountIndex] = { ...updatedAccount };
            setAccounts(updatedAccounts);
            setAccount(updatedAccount);
            alert("Account updated successfully!");
        } else {
            alert("Account not found.");
        }
    };
  return (
    <main>
      {account === null ? (
        <section>
          <form onSubmit={handleRegister}>
            <h1>Registration</h1>
            <input type="email" name="email" required />
            <input type="password" name="pass" required />
            <button>Submit</button>
          </form>
          <form onSubmit={handleSignin}>
            <h1>Login</h1>
            <input type="email" name="email" required />
            <input type="password" name="pass" required />
            <button>Submit</button>
          </form>
        </section>
      ) : (
        <section>
          <h1>Hello {account.email}</h1>
          <button onClick={logout}>Log out</button>

          {isEditing ? (
            <div>
              <h2>Edit Student</h2>
              <input
                type="text"
                name="name"
                value={editedStudent.name}
                onChange={handleEditChange}
                placeholder="Name"
              />
              <input
                type="text"
                name="lastname"
                value={editedStudent.lastname}
                onChange={handleEditChange}
                placeholder="Lastname"
              />
              <input
                type="number"
                name="age"
                value={editedStudent.age}
                onChange={handleEditChange}
                placeholder="Age"
              />
              <button onClick={handleUpdateStudent}>Update</button>
              <button onClick={() => {
                  setIsEditing(false);
                  setEditingIndex(null);
                  setEditedStudent({ name: "", lastname: "", age: "" });
              }}>Cancel</button>
            </div>
          ) : (
            <div>
              <form onSubmit={addStudent}>
                <input
                  type="text"
                  name="studentName"
                  placeholder="student name"
                  required
                />
                <input
                  type="text"
                  name="studentLastname"
                  placeholder="student lastname"
                  required
                />
                <input
                  type="number"
                  name="studentAge"
                  placeholder="student age"
                  required
                />
                <button>Add Student</button>
              </form>
            </div>
          )}

          <table>
            <thead>
              <tr>
                <th>Firstname</th>
                <th>Lastname</th>
                <th>Age</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {students.map((student, index) => (
                <tr key={index}>
                  <td>{student.name}</td>
                  <td>{student.lastname}</td>
                  <td>{student.age}</td>
                  <td>
                    <button onClick={() => editStudent(index)}>Edit</button>
                    <button onClick={() => deleteStudent(index)}>Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
                <div>
                    <h2>Edit Account</h2>
                    <form onSubmit={handleEditAccount}>
                        <input type="email" name="email" defaultValue={account.email} required />
                        <input type="password" name="pass" defaultValue={account.pass} required />
                        <button type="submit">Update Account</button>
                    </form>
                </div>
        </section>
      )}
    </main>
  );
}
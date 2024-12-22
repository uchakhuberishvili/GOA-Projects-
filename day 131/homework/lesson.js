import React, { useState } from "react";

const NameList = ({ names }) => (
  <ul>
    {names.map((name, index) => (
      <li key={index}>{name}</li>
    ))}
  </ul>
);

const Greeting = ({ name }) => <h2>გამარჯობა, {name}!</h2>;

const InputField = ({ sendDataToParent }) => {
  const handleInputChange = (event) => {
    sendDataToParent(event.target.value);
  };
  return <input type="text" placeholder="შეიყვანეთ მონაცემი" onChange={handleInputChange} />;
};

const App = () => {
  const names = ["ლუკა", "ანა", "გიორგი", "მარიამი"];
  const myName = "ლუკა";
  const [inputValue, setInputValue] = useState("");
  const receiveDataFromChild = (data) => setInputValue(data);

  return (
    <div>
      <h1>სახელების სია:</h1>
      <NameList names={names} />
      <Greeting name={myName} />
      <h1>შვილიდან მიღებული მონაცემი: {inputValue}</h1>
      <InputField sendDataToParent={receiveDataFromChild} />
    </div>
  );
};

export default App;

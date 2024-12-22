import React, { useState } from "react";
import InputField from "./InputField";

const App = () => {
  const [inputValue, setInputValue] = useState("");

  const receiveDataFromChild = (data) => {
    setInputValue(data);
  };

  return (
    <div>
      <h1>შვილიდან მიღებული მონაცემი: {inputValue}</h1>
      <InputField sendDataToParent={receiveDataFromChild} />
    </div>
  );
};


const InputField = ({ sendDataToParent }) => {
    const handleInputChange = (event) => {
      sendDataToParent(event.target.value);
    };
  
    return (
      <input
        type="text"
        placeholder="შეიყვანეთ მონაცემი"
        onChange={handleInputChange}
      />
    );
  };
  
  export default InputField;
  
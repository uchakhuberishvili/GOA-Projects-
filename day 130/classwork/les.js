import React from "react";
import NameList from "./NameList";

const App = () => {
  const names = ["ლუკა", "ანა", "გიორგი", "მარიამი"];

  return (
    <div>
      <h1>სახელების სია:</h1>
      <NameList names={names} />
    </div>
  );
};

export default App;

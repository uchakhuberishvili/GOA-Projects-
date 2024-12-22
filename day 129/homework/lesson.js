import React from "react";
import ProfileList from "./components/ProfileList";

const App = () => {
  const users = [
    { name: "ucha", age: 15, occupation: "Software Developer" },
    { name: "luka", age: 20, occupation: "Graphic Designer" },
    { name: "giorgi", age: 22, occupation: "Product Manager" },
  ];

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ textAlign: "center" }}>User Profiles</h1>
      <ProfileList profiles={users} />
    </div>
  );
};

export default App;

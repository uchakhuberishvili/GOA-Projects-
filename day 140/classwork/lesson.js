import React, { useState } from "react";

const Dropdown = () => {
  const [selected, setSelected] = useState("Select an option");
  return (
    <div>
      <select onChange={(e) => setSelected(e.target.value)}>
        <option disabled>Select an option</option>
        <option>Option 1</option>
        <option>Option 2</option>
        <option>Option 3</option>
      </select>
      <h1>{selected}</h1>
    </div>
  );
};

export default Dropdown;

import React, { useState } from "react";

const CheckboxToggle = () => {
  const [checked, setChecked] = useState(false);
  return (
    <div>
      <input type="checkbox" onChange={() => setChecked(!checked)} />
      <h1>{checked ? "Checked" : "Unchecked"}</h1>
    </div>
  );
};

export default CheckboxToggle;

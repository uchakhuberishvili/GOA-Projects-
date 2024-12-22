import React, { useState } from "react";

const FilterList = () => {
  const [query, setQuery] = useState("");
  const items = ["rame", "skami", "kompi", "tavi"];
  return (
    <div>
      <input onChange={(e) => setQuery(e.target.value.toLowerCase())} />
      <ul>
        {items.filter((item) => item.toLowerCase().includes(query)).map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default FilterList;

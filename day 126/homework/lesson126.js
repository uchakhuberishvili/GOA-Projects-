const greeting = "Hello";
const name = "Alice";

function App() {
    return <h1>{`${greeting}, ${name}!`}</h1>;
}

ReactDOM.render(<App />, document.getElementById("root"));
const categories = [
    { name: "Fruits", items: ["Apple", "Banana", "Cherry"] },
    { name: "Vegetables", items: ["Carrot", "Lettuce", "Spinach"] },
];

function App() {
    return (
        <div>
            {categories.map((category, index) => (
                <div key={index}>
                    <h2>{category.name}</h2>
                    <ul>
                        {category.items.map((item, i) => (
                            <li key={i}>{item}</li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById("root"));

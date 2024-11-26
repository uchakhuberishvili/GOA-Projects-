const items = ["Apple", "Banana", "Cherry"];

function App() {
    return (
        <ul>
            {items.map((item, index) => (
                <li key={index}>{item}</li>
            ))}
        </ul>
    );
}

ReactDOM.render(<App />, document.getElementById("root"));

const isLoggedIn = true;

function App() {
    return <h1>{isLoggedIn ? "Welcome" : "Please log in"}</h1>;
}

ReactDOM.render(<App />, document.getElementById("root"));

const backgroundColor = "lightblue";

function App() {
    const style = {
        backgroundColor,
        padding: "20px",
        borderRadius: "8px",
    };

    return <div style={style}>Styled Div</div>;
}

ReactDOM.render(<App />, document.getElementById("root"));

function getGreeting(name) {
    return <h1>Hello, {name}!</h1>;
}

function App() {
    return <div>{getGreeting("Alice")}</div>;
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

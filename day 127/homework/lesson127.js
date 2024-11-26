function FetchData() {
    const [data, setData] = React.useState([]);
    const [loading, setLoading] = React.useState(true);

    React.useEffect(() => {
        fetch("https://jsonplaceholder.typicode.com/posts")
            .then((response) => response.json())
            .then((json) => {
                setData(json.slice(0, 10));
                setLoading(false);
            });
    }, []);

    return (
        <div>
            <h1>Posts</h1>
            {loading ? (
                <p>Loading...</p>
            ) : (
                <ul>
                    {data.map((post) => (
                        <li key={post.id}>
                            <strong>{post.title}</strong>
                            <p>{post.body}</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}

ReactDOM.render(<FetchData />, document.getElementById("root"));

function Form() {
    const [formData, setFormData] = React.useState({ name: "", email: "" });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Name: ${formData.name}, Email: ${formData.email}`);
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>
                    Name:
                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                    />
                </label>
            </div>
            <div>
                <label>
                    Email:
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                    />
                </label>
            </div>
            <button type="submit">Submit</button>
        </form>
    );
}

ReactDOM.render(<Form />, document.getElementById("root"));

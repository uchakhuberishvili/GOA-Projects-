// React: ეს ბიბლიოთეკა საშუალებას გაძლევთ შექმნათ კომპონენტები და მართოთ ვირტუალური DOM.
// ReactDOM: ეს ბიბლიოთეკა გამოიყენება React კომპონენტების რეალურ DOM-ში გამოსატანად.
// Babel: ეს ბიბლიოთეკა გარდაქმნის თანამედროვე JSX კოდს ჩვეულებრივ JavaScript-ში, რომელიც ბრაუზერებს ესმით.

// JSX: JavaScript-ის გაფართოება, რომელიც საშუალებას გაძლევთ დაწეროთ HTML-ის მსგავსი კოდი JavaScript-ში.
// JSX გარდაქმნის HTML-ს React-ის ფუნქციურ გამოძახებებად.

function App() {
    return (
        <div>
            <h1>React & JSX Example</h1>
            <p>This is a paragraph rendered using JSX syntax.</p>
            <p>JSX makes it easy to build UI components in React.</p>
            <button onClick={() => alert("Button 1 clicked!")}>Button 1</button>
            <button onClick={() => alert("Button 2 clicked!")}>Button 2</button>
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById("root"));

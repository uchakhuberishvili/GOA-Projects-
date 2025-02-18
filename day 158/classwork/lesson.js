const [books, setBooks] = useState([]);

useEffect(() => {
    fetch(booksApi)
        .then(response => response.json())
        .then(data => setBooks(data))
        .catch(error => console.error('Error fetching books:', error));
}, []);

useEffect(() => {
    console.log('state changed');
}, [myState]);
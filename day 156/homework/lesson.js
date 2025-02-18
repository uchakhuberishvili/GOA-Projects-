import React, { useState, useEffect } from 'react';

function BookLibrary() {
    const [books, setBooks] = useState([]);
    const [myLibrary, setMyLibrary] = useState([]);
    const booksApi = 'https://faker-api.vercel.app/api/books?_quantity=10';

    useEffect(() => {
        fetch(booksApi)
            .then(response => response.json())
            .then(data => setBooks(data))
            .catch(error => console.error('Error fetching books:', error));
    }, []);

    const addToMyLibrary = (book) => {
        if (!myLibrary.some(item => item.id === book.id)) {
            setMyLibrary([...myLibrary, book]);
        }
    };

    return (
        <div>
            <h1>Book Library</h1>

            <div className="book-list">
                {books.map(book => (
                    <div key={book.id} className="book-item">
                        <h3>{book.title}</h3>
                        <p>Author: {book.author}</p>
                        <button onClick={() => addToMyLibrary(book)}>Add to My Library</button>
                    </div>
                ))}
            </div>

            <h2>My Library</h2>
            <div className="my-library">
                {myLibrary.map(book => (
                    <div key={book.id} className="book-item">
                        <h3>{book.title}</h3>
                        <p>Author: {book.author}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default BookLibrary;
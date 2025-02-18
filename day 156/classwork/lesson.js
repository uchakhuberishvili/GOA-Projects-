// import React, { useState, useEffect } from 'react';

// function BookLibrary() {
//     const [books, setBooks] = useState([]);
//     const [myLibrary, setMyLibrary] = useState([]);
//     const booksApi = 'https://faker-api.vercel.app/api/books?_quantity=10';

//     useEffect(() => {
//         fetch(booksApi)
//             .then(response => response.json())
//             .then(data => setBooks(data))
//             .catch(error => console.error('Error fetching books:', error));
//     }, []);

//     const addToMyLibrary = (book) => {
//         if (!myLibrary.some(item => item.id === book.id)) {
//             setMyLibrary([...myLibrary, book]);
//         }
//     };

//     return
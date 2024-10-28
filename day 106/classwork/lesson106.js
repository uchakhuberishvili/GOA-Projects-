const getBook = new Promise((resolve, reject) => {
    let friendBroughtBook = true;
    
    if (friendBroughtBook) {
        resolve("წიგნი წარმატებით მივიღეთ!");
    } else {
        reject("წიგნი ვერ მივიღეთ.");
    }
});

getBook
    .then((message) => console.log(message))
    .catch((error) => console.log(error));


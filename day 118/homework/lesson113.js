class Book extends CatalogEntry {
    constructor(title, year, author, genre) {
        super(title, year);
        this.author = author;
        this.genre = genre;
    }

    getDescription() {
        return `"${this.title}" by ${this.author} (${this.year}) - Genre: ${this.genre}.`;
    }
}

class Magazine extends CatalogEntry {
    constructor(title, year, issueNumber) {
        super(title, year);
        this.issueNumber = issueNumber;
    }

    getDescription() {
        return `"${this.title}" - Issue #${this.issueNumber}, published in ${this.year}.`;
    }
}

const myBook = new Book("The Great Gatsby", 1925, "F. Scott Fitzgerald", "Classic Fiction");
const myMagazine = new Magazine("National Geographic", 2023, 12);

console.log(myBook.getDescription());
console.log(myMagazine.getDescription());

myBook.checkOut();
myBook.checkOut();
myBook.returnToCatalog();
myBook.returnToCatalog(); 

myMagazine.checkOut();
myMagazine.returnToCatalog();

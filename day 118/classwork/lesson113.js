class CatalogEntry {
    constructor(title, year) {
        this.title = title;
        this.year = year;
        this.isAvailable = true; // Defaults to available
    }

    checkOut() {
        if (this.isAvailable) {
            this.isAvailable = false;
            console.log(`You've successfully checked out "${this.title}".`);
        } else {
            console.log(`"${this.title}" is currently checked out.`);
        }
    }

    returnToCatalog() {
        if (!this.isAvailable) {
            this.isAvailable = true;
            console.log(`"${this.title}" has been returned and is now available.`);
        } else {
            console.log(`"${this.title}" is already in the catalog.`);
        }
    }
}

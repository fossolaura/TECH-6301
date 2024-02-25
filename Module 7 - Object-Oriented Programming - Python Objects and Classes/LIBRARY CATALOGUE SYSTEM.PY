#Requirements

#Build a library catalogue system that manages information about books, 
#including their title, author, and availability status. Use classes to 
#represent books and include methods for checking out and returning books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.title} by {self.author} has been checked out.")
        else:
            print(f"{self.title} is currently unavailable.")

    def return_book(self):
        self.is_available = True
        print(f"{self.title} has been returned and is now available.")

class LibraryCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added {title} by {author} to the catalogue.")

    def display_catalogue(self):
        print("Library Catalogue:")
        for book in self.books:
            availability = "Available" if book.is_available else "Checked out"
            print(f"- {book.title} by {book.author} - {availability}")

def main():
    # Create the library catalogue
    catalogue = LibraryCatalogue()

    # Adding new books to the catalogue
    catalogue.add_book("Duma Key", "Stephen King")
    catalogue.add_book("The Book of Negroes", "Lawrence Hill")
    catalogue.add_book("The Glass Castle", "Jeannette Walls")
    catalogue.add_book("Hamlet", "William Shakespeare")
    catalogue.add_book("Holes", "Louis Sachar")
    catalogue.add_book("Lord Of The Flies", "William Golding")
    catalogue.add_book("Macbeth", "William Shakespeare")

    # Print initial catalogue
    catalogue.display_catalogue()

    # Interacting with the catalogue
    # Checking out a book
    catalogue.books[0].check_out()

    # Trying to check out the same book again
    catalogue.books[0].check_out()

    # Returning a book
    catalogue.books[0].return_book()

    # Print final catalogue
    catalogue.display_catalogue()

if __name__ == "__main__":
    main()
    
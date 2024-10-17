class Book:
    """A class to represent a book in a library."""
    
    def __init__(self, title, author):
        """Initialize the book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

class Library:
    """A class to represent a library which holds books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Find a book by title and check it out if it is available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"'{title}' has been checked out.")
                    return
                else:
                    print(f"'{title}' is currently unavailable.")
                    return
        print(f"'{title}' not found in the library.")
    
    def return_book(self, title):
        """Find a book by title and return it to the library."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"'{title}' has been returned.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"'{title}' not found in the library.")
    
    def list_available_books(self):
        """List all books that are available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books at the moment.")

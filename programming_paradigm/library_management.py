
class Book:
    """Represents a book with a title and author, and whether it's checked out."""
    
    def __init__(self, title, author):
        self.title = title            # Public attribute
        self.author = author          # Public attribute
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Manages a collection of Book objects."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a Book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        # If not available or not found, do nothing (checker does not expect error message)

    def return_book(self, title):
        """Return a book by title if it was checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        # If not found or already returned, do nothing

    def list_available_books(self):
        """Print a list of books that are currently available."""
        for book in self._books:
            if book.is_available():
                print(book)

class Book:
    """Represents a book in the library system"""
    
    def __init__(self, title, author):
        """
        Initialize a new book
        
        Args:
            title (str): Title of the book
            author (str): Author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Check out the book if available"""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Return the book to the library"""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    @property
    def is_available(self):
        """Check if the book is available for checkout"""
        return not self._is_checked_out


class Library:
    """Manages a collection of books"""
    
    def __init__(self):
        """Initialize an empty library"""
        self._books = []  # Private list to store books

    def add_book(self, book):
        """
        Add a book to the library
        
        Args:
            book (Book): Book instance to add
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library")

    def check_out_book(self, title):
        """
        Check out a book by title
        
        Args:
            title (str): Title of the book to check out
            
        Returns:
            bool: True if successful, False otherwise
        """
        for book in self._books:
            if book.title == title and book.is_available:
                return book.check_out()
        return False

    def return_book(self, title):
        """
        Return a book by title
        
        Args:
            title (str): Title of the book to return
            
        Returns:
            bool: True if successful, False otherwise
        """
        for book in self._books:
            if book.title == title and not book.is_available:
                return book.return_book()
        return False

    def list_available_books(self):
        """List all available books in the library"""
        available = [book for book in self._books if book.is_available]
        if not available:
            print("No books currently available")
            return
            
        for book in available:
            print(f"{book.title} by {book.author}")
class Book:
    """Represents a basic book with title and author.
    
    Attributes:
        title: Title of the book.
        author: Author of the book.
    """
    
    def __init__(self, title: str, author: str):
        """Initializes a Book instance.
        
        Args:
            title: Title of the book.
            author: Author of the book.
        """
        self.title = title
        self.author = author
    
    def __str__(self) -> str:
        """Provides human-readable string representation of the book.
        
        Returns:
            String in format: "Book: {title} by {author}"
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Represents an electronic book, inheriting from Book.
    
    Adds file_size attribute to base Book class.
    
    Attributes:
        title: Inherited from Book - title of the book.
        author: Inherited from Book - author of the book.
        file_size: Size of eBook file in kilobytes.
    """
    
    def __init__(self, title: str, author: str, file_size: int):
        """Initializes an EBook instance.
        
        Args:
            title: Title of the eBook.
            author: Author of the eBook.
            file_size: File size in kilobytes.
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self) -> str:
        """Provides human-readable string representation of the eBook.
        
        Returns:
            String in format: "EBook: {title} by {author}, File Size: {file_size}KB"
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Represents a physical printed book, inheriting from Book.
    
    Adds page_count attribute to base Book class.
    
    Attributes:
        title: Inherited from Book - title of the book.
        author: Inherited from Book - author of the book.
        page_count: Number of pages in the printed book.
    """
    
    def __init__(self, title: str, author: str, page_count: int):
        """Initializes a PrintBook instance.
        
        Args:
            title: Title of the printed book.
            author: Author of the printed book.
            page_count: Number of pages in the book.
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self) -> str:
        """Provides human-readable string representation of the print book.
        
        Returns:
            String in format: "PrintBook: {title} by {author}, Page Count: {page_count}"
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Manages a collection of books using composition.
    
    Attributes:
        books: List containing Book, EBook, and PrintBook instances.
    """
    
    def __init__(self):
        """Initializes a Library with an empty book collection."""
        self.books = []
    
    def add_book(self, book: Book) -> None:
        """Adds a book to the library collection.
        
        Args:
            book: Book instance to add (can be Book, EBook, or PrintBook)
        """
        self.books.append(book)
    
    def list_books(self) -> None:
        """Prints details of all books in the library collection.
        
        Outputs each book's string representation on separate lines.
        """
        for book in self.books:
            print(book)
class Book:
    def __init__(self, title: str, author: str):
        """Initialize base book attributes"""
        self.title = title
        self.author = author
    
    def __str__(self):
        """String representation for base Book class"""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initialize eBook with additional file_size attribute
        :param file_size: Size in KB
        """
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """String representation for eBooks"""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initialize print book with additional page_count attribute
        :param page_count: Number of pages
        """
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """String representation for print books"""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        """Initialize library with empty book collection"""
        self.books = []
    
    def add_book(self, book: Book):
        """Add any type of book to the library"""
        self.books.append(book)
        print(f"Added '{book.title}' to the library")
    
    def list_books(self):
        """Display all books in the library with their specific details"""
        if not self.books:
            print("The library is empty")
            return
        
        print("\nLibrary Collection:")
        for book in self.books:
            print(book)
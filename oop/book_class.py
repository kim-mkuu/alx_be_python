class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor for Book class
        :param title: Title of the book
        :param author: Author of the book
        :param year: Publication year
        """
        self.title = title
        self.author = author
        self.year = year
        
    def __del__(self):
        """Destructor that prints deletion message"""
        print(f"Deleting {self.title}")
        
    def __str__(self):
        """User-friendly string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official representation that can recreate the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
import math

class Shape:
    """Base class representing a geometric shape"""
    
    def area(self) -> float:
        """Calculate the area of the shape
        
        Raises:
            NotImplementedError: If called directly on base class
        """
        raise NotImplementedError("Subclasses must implement area() method")

class Rectangle(Shape):
    """Rectangle shape derived from Shape base class"""
    
    def __init__(self, length: float, width: float):
        """Initialize rectangle with length and width
        
        Args:
            length: Length of the rectangle
            width: Width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """Calculate rectangle area (length × width)"""
        return self.length * self.width

class Circle(Shape):
    """Circle shape derived from Shape base class"""
    
    def __init__(self, radius: float):
        """Initialize circle with radius
        
        Args:
            radius: Radius of the circle
        """
        self.radius = radius
    
    def area(self) -> float:
        """Calculate circle area (π × radius²)"""
        return math.pi * self.radius ** 2
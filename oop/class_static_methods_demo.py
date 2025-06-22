class Calculator:
    """Demonstrates class methods and static methods"""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Static method to add two numbers
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """Class method to multiply two numbers
        
        Args:
            cls: Reference to the class
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
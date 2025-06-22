class Calculator:
    """A class demonstrating class methods and static methods.
    
    Attributes:
        calculation_type: A class-level string describing the type of calculations.
    """
    
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """Add two numbers.
        
        This static method performs addition without accessing class or instance state.
        
        Args:
            a: First number to add
            b: Second number to add
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Multiply two numbers.
        
        This class method accesses class-level state before performing multiplication.
        
        Args:
            cls: Reference to the Calculator class
            a: First number to multiply
            b: Second number to multiply
            
        Returns:
            Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
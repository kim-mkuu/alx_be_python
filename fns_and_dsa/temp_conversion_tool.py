# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global conversion factor"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global conversion factor"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    print("Temperature Conversion Tool")
    
    # Get temperature input with validation
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    # Get unit input with validation
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit not in ['C', 'F']:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return
    
    # Perform conversion based on unit
    if unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    else:  # unit == 'C'
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")

if __name__ == "__main__":
    main()
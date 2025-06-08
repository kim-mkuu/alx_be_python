from datetime import datetime, timedelta

def display_current_datetime():
    """Display current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date

def calculate_future_date(days):
    """Calculate and return future date after specified days"""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_date}")
    return future_date

def main():
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Calculate future date
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days = int(days_input)
        calculate_future_date(days)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer for days.")

if __name__ == "__main__":
    main()
# Script to calculate user's future age

# Prompt the user to input their current age
current_age_str = input("How old are you? ")

# Convert the input string to an integer
current_age = int(current_age_str)

# Calculate the age in 2050. Assume the current year is 2023, so add 27 years.
age_in_2050 = current_age + 27

# Print the user's age in 2050 in the specified format
print(f"In 2050, you will be {age_in_2050} years old.")
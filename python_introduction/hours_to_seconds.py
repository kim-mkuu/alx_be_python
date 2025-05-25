# Script for converting hours to seconds
hours = 2

# Time unit conversion breakdown
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = seconds_per_minute * minutes_per_hour  # 60 * 60 = 3600

# Convert hours to seconds
seconds = hours * seconds_per_hour

# Print the result
print(f"{hours} hour(s) is {seconds} seconds")
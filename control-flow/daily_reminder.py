# Get task input
task = input("Enter your task: ")

# Validate priority input with loop
while True:
    priority = input("Priority (high/medium/low): ").strip().lower()
    if priority in ('high', 'medium', 'low'):
        break

# Validate time-bound input with loop
while True:
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
    if time_bound in ('yes', 'no'):
        break

# Process using match-case with catch-all
match priority:
    case 'high' | 'medium' | 'low':
        if time_bound == 'yes':
            reminder = f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time."
    case _:
        # Fallback for unexpected priority (though validation prevents this)
        if time_bound == 'yes':
            reminder = f"Reminder: '{task}' requires immediate attention today!"
        else:
            reminder = f"Note: Consider completing '{task}' when you have free time."

# Output final reminder
print("\n" + reminder)
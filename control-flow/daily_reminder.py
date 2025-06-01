# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Determine base reminder message
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Note: '{task}' is a medium priority task. Try to get it done soon."
    case "low":
        reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Warning: '{task}' has an unrecognized priority level."

# Ensure a fully customized reminder based on time sensitivity
if time_bound == "yes":
    reminder += " That requires immediate attention today!"

# Provide the final customized reminder
print(reminder)


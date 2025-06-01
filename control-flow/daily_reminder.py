# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Determine task priority only (without extra messages)
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = f"Reminder: '{task}' has an unrecognized priority level."

# Customize the reminder based on time sensitivity
if time_bound == "yes":
    reminder += " That requires immediate attention today!"
elif priority == "low":
    reminder += " Consider completing it when you have free time."
elif priority == "medium":
    reminder += " Try to get it done soon."

# Display the final customized reminder
print(reminder)

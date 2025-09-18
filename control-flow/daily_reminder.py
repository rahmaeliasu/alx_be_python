task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Using match-case to handle different priority levels and time-bound status
match priority:
    case "high":
        message = "high"
    case "medium":
        message = "medium"
    case "low":
        message = "low"
    case _:
        print("Error: Invalid priority level. Please enter high, medium, or low.")

if time_bound == "yes" or 'y' and message == "high":
    print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
else:
    print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")

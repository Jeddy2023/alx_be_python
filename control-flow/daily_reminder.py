# Step 1: Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  # Ensure the input is lowercase
time_bound = input("Is it time-bound? (yes/no): ").lower()  # Ensure the input is lowercase

# Step 2: Provide the reminder based on task priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unrecognized priority level."

# Step 3: Modify the reminder based on whether the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Step 4: Print the customized reminder with the exact wording
print(f"Reminder: {reminder}")

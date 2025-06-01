#prompt user to enter a single task
task = input("Enter your task: ")
#prompt user to enter the task's priority
Priority = input("Priority (high/medium/low): ")
#is the task time-bound
time_bound = input("Is it time-bound? (yes/no): ")
#process task based on priority and time sensitivity
match Priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}'This is a high-priority task that requires immediate attention today!.")
        else:
            print(f"Reminder: '{task}' This is a high-priority task.Consider completing it when you have free time")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' This is a medium-priority task that requires immediate attention today!.")
        else:
            print(f"Reminder: '{task}' This is a medium-priority task. Consider completing it when you have free time")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' This is a low-priority task that requires immediate attention today!.")
        else:
            print(f"Reminder: '{task}' This is a low-priority task. Consider completing it when you have free time.")
        

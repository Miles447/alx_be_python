#prompt user to enter a single task
Task = input("Enter your Task: ")
#prompt user to enter the task's priority
Priority = input("Priority(high/medium/low): ")
#is the task time-bound
Time_Bound = input("Is it Time Bound?(yes/no): ")
#process task based on priority and time sensitivity
match Priority:
    case "high":
        print("This is a high-priority task.")
    case "medium":
        print("This is a medium-priority task.")
    case "low":
        print("This is a low-priority task.")
if Time_Bound == "yes":
    print("requires immediate attention today")
elif Time_Bound == "no":
    print("consider completing it when you have free time")
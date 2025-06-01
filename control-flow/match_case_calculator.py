#prompt the user to enter two numbers and an operator.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
#implement a simple calculator using match-case.
match operator:
    case "add":
        result = num1 + num2
        print(f"The result is: {result}")
    case "subtract":
        result = num1 - num2
        print(f"The result is: {result}")
    case "multiply":
        result = num1 * num2
        print(f"The result is: {result}")
    case "divide":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is: {result}")
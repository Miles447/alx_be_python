def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator /  denominator
        print ("f{result}is the result")

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    try:
        numerator = float(numerator)
        denominator =float(denominator)

        result = numerator / denominator
        print ("f{result} is the result")
    except ValueError:
        return"Error: Please enter valid numeric inputs"

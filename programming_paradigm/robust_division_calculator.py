def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator /  denominator
        print ("f{result}is the result")

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    try:
        numerator = float(numerator)
        denominator =float(denominator)

        result = numerator / denominator
        print ("f{result} is the result")
    except ValueError:
        return "Error: Please enter numeric values only."

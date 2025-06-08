# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Use global factor to convert Fahrenheit to Celsius
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # Use global factor to convert Celsius to Fahrenheit
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:
        print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

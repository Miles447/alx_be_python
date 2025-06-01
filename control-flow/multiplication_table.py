#prompt the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))
#use a for loop to generate a amultiplication table

for y in range(1, 10+1):
    print(f"{number} x {y} = {number * y}")

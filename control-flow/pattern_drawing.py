#prompting the user to enter a positive integer
x = int(input("Enter the size of the pattern: "))

#using a nested loop to draw a pattern
row = 0
while row < x:
    for col in range(x):
        print("*", end="")
    print()
    row += 1
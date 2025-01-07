# Objectives
# Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
# Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions met or and else when no condition is met.



# Stretch Goals (Optional Objectives)
# Pursue stretch goals if you are a more advanced user or have remaining lab time.

# Create an if statement with two conditions by using and between conditions.

# Create an if statement with two conditions by using or between conditions.

# Create a nested if statement.

# Hint:  a = int(input("Enter a number "))

# Ask the user to input two numbers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Compare the two numbers
if a == b:
    print("a is equal to b.")
elif a > b:
    print("a is greater than b.")
else:
    print("a is less than b.")

# Check if both numbers are positive
if a > 0 and b > 0:
    print("Both numbers are positive.")

# Check if at least one number is even
if a % 2 == 0 or b % 2 == 0:
    print("At least one number is even.")

# Nested condition: Check if a is much larger than b
if a > b:
    if a - b > 10:
        print("a is much larger than b (difference > 10).")

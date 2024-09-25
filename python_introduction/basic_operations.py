# This script performs basic arithmetic operations: addition, subtraction, and multiplication
# It uses two predefined numbers, number1 and number2, and prints the results in a formatted manner.

# Step 1: Define the two variables with specific values
# number1 is the first number for the operations
number1 = 10

# number2 is the second number for the operations
number2 = 5

# Step 2: Perform arithmetic operations

# Addition of number1 and number2
# The '+' operator is used to add the two numbers
addition = number1 + number2

# Subtraction of number2 from number1
# The '-' operator is used to subtract number2 from number1
subtraction = number1 - number2

# Multiplication of number1 and number2
# The '*' operator is used to multiply the two numbers
multiplication = number1 * number2

# Step 3: Print the results of each operation

# The result of the addition is printed using an f-string for formatted output
# This ensures the result is displayed in a clear, readable format
print(f"Addition of {number1} and {number2} is {addition}")

# The result of the subtraction is printed in the same way
# The output will show the difference between number1 and number2
print(f"Subtraction of {number1} and {number2} is {subtraction}")

# The result of the multiplication is printed next
# The output will display the product of number1 and number2
print(f"Multiplication of {number1} and {number2} is {multiplication}")

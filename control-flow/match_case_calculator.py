# This script performs basic arithmetic operations using a match-case statement.

# Step 1: Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))  # Convert the input to a float
num2 = float(input("Enter the second number: ")) # Convert the input to a float

# Step 2: Prompt the user to choose an arithmetic operation
operation = input("Choose the operation (+, -, *, /): ")

# Step 3: Use a match-case statement to perform the chosen operation
match operation:
    case '+':  # Addition
        result = num1 + num2
        print(f"The result is {result}.")
    
    case '-':  # Subtraction
        result = num1 - num2
        print(f"The result is {result}.")
    
    case '*':  # Multiplication
        result = num1 * num2
        print(f"The result is {result}.")
    
    case '/':  # Division
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    
    case _:  # Default case for invalid operations
        print("Invalid operation. Please choose one of +, -, *, /.")

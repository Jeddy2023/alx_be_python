# Define the perform_operation function
def perform_operation(num1, num2, operation):
    # Perform the arithmetic operation based on the provided operation parameter
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        # Handle division by zero
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"

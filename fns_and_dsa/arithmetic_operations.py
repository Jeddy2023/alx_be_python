# Define the perform_operation function
def perform_operation(num1, num2, operation):
    # Perform the arithmetic operation based on the provided operation parameter
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            # Handle division by zero
            if num2 == 0:
                return "Cannot divide by zero"
            else:
                return num1 / num2
        case _:
            return "Invalid operation"

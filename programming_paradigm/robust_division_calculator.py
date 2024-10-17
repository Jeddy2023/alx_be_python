def safe_divide(numerator, denominator):
    """Perform division while handling division by zero and non-numeric inputs."""
    try:
        # Attempt to convert the inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Check for division by zero
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        # Perform the division
        result = num / denom
        return f"The result of the division is {result:.2f}"

    except ValueError:
        # Handle non-numeric input errors
        return "Error: Please enter numeric values only."

# This script draws a square pattern of asterisks based on user input.

# Step 1: Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Step 2: Use a while loop to control the number of rows
row = 0  # Initialize the row counter

while row < size:
    # Step 3: Use a for loop to print the asterisks for each row
    for col in range(size):
        print("*", end="")  # Print asterisk without advancing to the next line
    print()  # Print a newline after the row is complete
    row += 1  # Move to the next row

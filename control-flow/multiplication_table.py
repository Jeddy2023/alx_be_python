# This script generates a multiplication table for a user-specified number.

# Step 1: Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Use a for loop to generate and print the multiplication table from 1 to 10
for i in range(1, 11):
    product = number * i  # Calculate the product of the number and the current iterator i
    print(f"{number} * {i} = {product}")  # Print the multiplication in the desired format

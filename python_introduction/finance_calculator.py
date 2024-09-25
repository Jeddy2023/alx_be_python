# This script calculates the user's monthly savings and projects annual savings with interest.

# Step 1: Prompt the user for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Step 2: Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Step 3: Project annual savings with a 5% interest rate
# Formula: Projected Savings = (Monthly Savings * 12) + (Monthly Savings * 12 * 0.05)
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Step 4: Output the results
print(f"Your monthly savings are: ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

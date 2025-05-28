#Personal Finance Calculator

# Prompt the user for their monthly income
monthly_income_str = input("Enter your monthly income: ")
monthly_income = float(monthly_income_str) # Using float to allow for decimal incomes

# Total monthly expenses
monthly_expenses_str = input("Enter your total monthly expenses: ")
monthly_expenses = float(monthly_expenses_str) # Using float for expenses as well

# Monthly Savings calculation
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
# Assume a simple annual interest rate of 5% (0.05)
# Simplified formula: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Show projected savings
print(f"Your monthly savings are ${monthly_savings:.2f}.") # .2f for two decimal places
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")
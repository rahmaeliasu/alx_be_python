monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
# Assuming a 5% interest rate on savings
annual_savings_projection = monthly_savings * 12 + int((monthly_savings * 12 * 0.05))

print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(annual_savings_projection) + ".")

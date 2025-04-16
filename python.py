
price_per_bracelet = 750
bracelets_made = 20
materials_cost = 3000
delivery_cost = 1500
packaging_cost = 500
discount_given = 250
saving_percentage = 0.20

total_income = price_per_bracelet * bracelets_made - discount_given
total_expenses = materials_cost + delivery_cost + packaging_cost
profit = total_income - total_expenses
amount_saved = profit * saving_percentage

print("Total Income:", total_income)
print("Total Expenses:", total_expenses)
print("Profit:", profit)
print("Amount Saved:", amount_saved)

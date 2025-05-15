
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

# 4. List of items Zara might need for her bracelet business

items = ["beads", "strings", "glue", "scissors", "charms"]

# a. Print the first and last item
print("First item:", items[0])
print("Last item:", items[-1])

# b. Add a new item
items.append("clasps")

# c. Remove one item
items.remove("scissors")

# d. Print the number of items in the list
print("Number of items:", len(items))


# Correct way to handle the apostrophe
greeting = "Hello, my name is John and I’m learning Python."

# Correct way to handle quotes inside quotes
quote = 'She said, "Python is easy to learn."'

# No problem here, but a space will make it nicer
name = 'Musa'
print("Hello " + name)

# Correct multi-line string
story = """Today was a good day,
I learned about variables."""


# Ask the user for the cost of the meal.
mealCost = float(input("Enter the cost of the meal: "))

# Calculate the tip, sales tax, and total cost.
tip = mealCost * 0.18
tax = mealCost * 0.07
total = mealCost + tip + tax

# Store the results in a list and display each amount.
amounts = [
    ("Meal cost", mealCost),
    ("Tip (18%)", tip),
    ("Sales tax (7%)", tax),
    ("Total cost", total),
]

for label, amount in amounts:
    print(f"{label}: ${amount:.2f}")

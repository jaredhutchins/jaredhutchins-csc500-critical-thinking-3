# Ask the user for the cost of the meal.
mealCost = float(input("Enter the cost of the meal: "))

# Calculate the tip, sales tax, and total cost.
tip = mealCost * 0.18
tax = mealCost * 0.07
total = mealCost + tip + tax

# Display the results.
print(f"Meal cost: ${mealCost:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales tax (7%): ${tax:.2f}")
print(f"Total cost: ${total:.2f}")

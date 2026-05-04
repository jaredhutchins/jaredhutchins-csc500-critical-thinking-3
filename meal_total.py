# Ask the user for the cost of the meal.
meal_cost = float(input("Enter the cost of the meal: "))

if meal_cost < 0:
    print("Error: Meal cost must be 0 or greater.")
else:
    # Calculate the tip, sales tax, and total cost.
    tip = meal_cost * 0.18
    tax = meal_cost * 0.07
    total = meal_cost + tip + tax

    # Store the results in a list and display each amount.
    amounts = [
        ("Meal cost", meal_cost),
        ("Tip (18%)", tip),
        ("Sales tax (7%)", tax),
        ("Total cost", total),
    ]

    for label, amount in amounts:
        print(f"{label}: ${amount:.2f}")

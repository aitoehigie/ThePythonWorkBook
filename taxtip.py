#!/usr/bin/env python

meal_cost = float(input("How much does the meal cost?:"))

tax_rate = 0.05

tip_rate = 0.18

tip = round((tip_rate * meal_cost), 2)

tax = round((tax_rate * meal_cost), 2)

total = round(meal_cost + tip + tax)

print(f"""
Break down of the cost of your meal
###################################
Tax: ${tax}
Tip: ${tip}
Grand Total: ${total}
""")

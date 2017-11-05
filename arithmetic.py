#!/usr/bin/env python
import math

a = int(input("enter a value for a:"))
b = int(input("enter a value for b:"))
sum = a + b
difference = b - a
product = a * b
quotient = a // b
remainder = a % b
log = math.log(a)
power = math.pow(a, b)

print(f"""
Sum of {a} and {b}: {sum}
Difference between {a} and {b}: {difference}
Product of {a} and {b}: {product}
Quotient when {a} is divided by {b}: {quotient}
Remainder when {a} is divided by {b}: {remainder}
log10{a}: {log}
{a} ^ {b}: {power}
""")





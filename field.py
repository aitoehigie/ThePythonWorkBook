#!/usr/bin/env python

length: float = float(input("Length of the field in feet:"))
breadth: float = float(input("Width of the field in feet:"))
square_feet_per_acre = 43560
area = length * breadth
area_in_acres = area/square_feet_per_acre

print(f"The area of the field is {area_in_acres} acres")

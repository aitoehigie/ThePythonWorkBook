#!/usr/bin/env python

length: float = float(input("Length of the field in feet:"))
breadth: float = float(input("Width of the field in feet:"))

area = length * breadth
area_in_acres = area/43560

print(f"The area of the field is {area_in_acres} acres")

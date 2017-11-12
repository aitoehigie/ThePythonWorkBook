#!/usr/bin/env python

def reverse_order():
    numbers = []
    number = int(input("Enter a number (0 to quit):"))
    while number != 0:
        numbers.append(number)
        number = int(input("Enter a number (0 to quit):"))
    numbers.reverse()
    return numbers

if __name__ == "__main__":
    for item in reverse_order():
        print(item, "\n")



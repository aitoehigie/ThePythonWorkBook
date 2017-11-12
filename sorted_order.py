#!/usr/bin/env python3

def sorted():
    numbers = []
    number = int(input("Enter a number (0 to quit):"))
    while number != 0:
        numbers.append(number)
        number = int(input("Enter a number:"))
    return numbers


if __name__ == "__main__":
    print(sorted())

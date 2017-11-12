#!/usr/bin/env python3

def sorted():
    numbers = []
    number = int(input("Enter a number (0 to quit):"))
    while number != 0:
        numbers.append(number)
        number = int(input("Enter a number:"))
    numbers.sort()
    return numbers


if __name__ == "__main__":
    for number in sorted():
        print(number, "\n")


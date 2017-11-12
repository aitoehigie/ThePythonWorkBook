#!/usr/bin/env python3

result = []

words = input("Enter a word (blank line to quit):")

while words != "":
    result.append(words)
    words = input("Enter a word (blank line to quit):")
else:
    pass

if __name__ == "__main__":
    for name in result:
        print(name, "\n")    

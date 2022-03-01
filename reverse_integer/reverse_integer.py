"""
Given an integer, return the integer with reversed digits.
Note: The integer could be either positive or negative.
"""


number = input("enter a number ")

if number[0] == "-":
    print(f"-{number[:0:-1]}")
else:
    print(int(number[::-1]))

""""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

Notes:

Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.

num1 = '364'
num2 = '1836'

Output:
2200
2200
"""

num1 = '364'
num2 = '1836'

def solution(number1: str, number2: str):
    print(str(eval(number1) + eval(number2)))

solution(num1, num2)
"""
Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1. # Note: all the input strings are already lowercase.
"""


def solution(word: str):
    frequency = {}
    for letter in word:
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1

    return next((word.index(k) for k, v in frequency.items() if v == 1), -1)


print(solution('alphabet'))
print(solution('barbados'))
print(solution('crunchy'))
print(solution('chui'))

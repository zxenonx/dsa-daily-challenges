"""
For a given sentence, return the average word length. 
Note: Remember to remove punctuation first.

Input
sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

Output
4.2
4.08
"""

import re
from string import punctuation

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"


def solution(sentence: str):
    """Average word length with replace() and split()

    Args:
        sentence (str): The given sentence
    """
    for element in punctuation:
        if element in sentence:
            sentence = sentence.replace(element, "")
    words = sentence.split(" ")
    words_total = sum(len(word) for word in words)
    print(round(words_total/len(words), 2))


solution(sentence1)
solution(sentence2)


def solution2(sentence: str):
    """Average word length with regex

    Args:
        sentence (str): The given sentence
    """
    new_sentence = sentence.translate(str.maketrans("", "", punctuation))
    words = new_sentence.split(" ")
    words_total = sum(len(word) for word in words)
    print(round(words_total/len(words), 2))


solution2(sentence1)
solution2(sentence2)


def solution3(sentence: str):
    """Average word length with regex

    Args:
        sentence (str): The given sentence
    """
    new_sentence = re.sub(r'[^\w\s]', "", sentence)
    words = new_sentence.split(" ")
    words_total = sum(len(word) for word in words)
    print(round(words_total/len(words), 2))


solution3(sentence1)
solution3(sentence2)

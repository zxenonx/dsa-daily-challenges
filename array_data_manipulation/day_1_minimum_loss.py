"""
Given an array of house prices, return the minimum loss

Input: [10, 5, 3]

Output: 2
"""
from typing import List


def min_loss(house_prices: List):
    """
    Given an array of house prices, return the minimum loss
    :param house_prices:
    :return:int
    """
    losses = [
        house_prices[i] - house_prices[i + 1]
        for i in range(len(house_prices) - 1)
    ]
    losses.sort()
    print(losses[0])


min_loss([10, 5, 3])
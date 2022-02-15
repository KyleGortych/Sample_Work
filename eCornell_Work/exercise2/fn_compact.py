"""  
A function to roll two dice
Reduced version

Author: Kyle Gortych
Date: 5/21/2021
"""
import random

def rollem(sum):
    """
    Returns the sum of two random numbers.
    """
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    sum = roll1 + roll2
    return sum

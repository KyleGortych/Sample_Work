"""
A simple die roller

Author: Kyle Gortych
Date: 2/23/2021
"""

import random

first = input("Type the first number: ")
first = int(first)

last = input("Type the last number: ")
last = int(last)

roll = random.randint(first,last)
print("Choosing a number between %s and %d." %(first,last))
print ("The number is %d." % roll)
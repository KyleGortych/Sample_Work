"""  
A module to demonstrate global variables.

Author: Kyle Gortych
Date: 5/21/2021
"""

# The global variable
VAR = 1

def next():
    """
    Returns and increments the value of VAR.
    """
    global VAR
    VAR += 1
    return VAR

"""
ex
Descript:
Functions as variables

File name:     ex.py
Maintainer:    Kyle Gortych
Created:       05-26-2022
Last Modified: xx-xx-xxxx
"""

def add_one(x):
    """ return: x + 1 """
    return x + 1

def minus_one(x):
    """ return: x - 1 """
    return x - 1

def resolve(f, arg):
    """ return: result of the fn call f(arg) """
    return f(arg)

a = resolve(add_one, 2)
b = resolve(minus_one, 2)
print('a: ' + str(a), '\nb: ' + str(b))

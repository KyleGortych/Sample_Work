"""
ex
Descript:
Functions as Arguments

File name:     ex.py
Maintainer:    Kyle Gortych
Created:       05-26-2022
Last Modified: xx-xx-xxxx
"""

def add_one(x):
    """ return: x + 1 """
    return x + 1

def minues_one(x):
    """ return: -x """
    return -x

def map(f,data):
    """ return: copy of data | f applied to each entry """
    accum = ()
    for item in data:
        accum = accum + (f(item), )
    return accum

a = (1, 2, 3)
b = map(add_one, a)
c = map(minues_one, a)
print('a: ' + str(a), '\nb: ' + str(b), '\nc: ' + str(c))

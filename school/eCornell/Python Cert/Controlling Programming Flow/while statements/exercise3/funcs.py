"""
Module with for-loops that loop over positions.

Author: Kyle Gortych
Date: 03/26/2022
"""

def skip(s,n):
    """
    Returns a copy of s, only including positions that are multiples of n

    A position is a multiple of n if pos % n == 0.

    Examples:
        skip('hello world',1) returns 'hello world'
        skip('hello world',2) returns 'hlowrd'
        skip('hello world',3) returns 'hlwl'
        skip('hello world',4) returns 'hor'

    Parameter s: the string to copy
    Precondition: s is a nonempty string

    Parameter n: the letter positions to accept
    Precondition: n is an int > 0
    """
    assert type(s) == str and len(s) > 0
    assert type(n) == int and n > 0
    # You must use a while-loop, not a for-loop
    var = []
    var2 = True
    pos = 0
    count = 1

    while var2:
        if pos % n == 0 and count <= len(s):
            var.append(s[pos])
            pos += 1
            count += 1
        elif pos % n != 0 and count <= len(s):
            pos += 1
            count += 1
        else:
            var2 = False
    return ''.join(var)
    #pass


def fixed_points(tup):
    """
    Returns a copy of tup, including only the "fixed points".

    A fixed point of a tuple is an element that is equal to its position in the tuple.
    For example 0 and 2 are fixed points of (0,3,2).  The fixed points are returned in
    the order that they appear in the tuple.

    Examples:
        fixed_points((0,3,2)) returns (0,2)
        fixed_points((0,1,2)) returns (0,1,2)
        fixed_points((2,1,0)) returns ()

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of ints
    """
    assert type(tup) == tuple
    # You must use a while-loop, not a for-loop
    var = list(tup)
    var2 = []
    pos = 0
    count = 1

    while count <= len(var):
        if pos == var[pos]:
            var2.append(var[pos])
        pos += 1
        count += 1
    return tuple(var2)
    #pass

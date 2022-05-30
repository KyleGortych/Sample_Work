"""
funcs
Descript:


File name:  funcs.py
Maintainer: Kyle Gortych
created:    03-21-2022
"""
def factorial(n):
    """
    Returns n! = n * (n-1) * (n-2) ... * 1

    0! is 1.  Factorial is undefined for integers < 0.

    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120

    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """
    assert type(n) == int
    assert n >= 0

    result = 1

    for i in range(1, n + 1):
        result = result * i
    return result

    #pass


def revrange(a,b):
    """
    Returns the tuple (b-1, b-2, ..., a)

    Note that this tuple is the reverse of tuple(range(a,b))

    Parameter a: the "start" of the range
    Precondition: a is an int <= b

    Parameter b: the "end" of the range
    Precondition: b is an int >= a
    """
    assert type(a) == int and a <= b
    assert type(b) == int

    tup1 = tuple(range(a,b))
    tup2 = tup1[::-1]
    tup = ()
    result = tup
    for i in tup2:
        if a < b:
            result = tup2
        else:
            result = tup
    return result
    #pass

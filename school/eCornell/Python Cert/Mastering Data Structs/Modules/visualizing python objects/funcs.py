"""
funcs
Descript:
left vs right associativity
For an algebra or more generally a field to be associative it must be 
the same for both left and right

∀f: add
-- inference -- 


File name:     funcs.py
Maintainer:    Kyle Gortych
Created:       05-26-2022
Last Modified: 05-28-2022
"""

def add(x,y):
    """
    Returns the sum x+y

    This works on any types that support addition (numbers, strings, etc.)

    Parameter x: The first value to add
    Precondition: x supports addition and x is same type as y

    Parameter x: The second value to add
    Precondition: x supports addition and x is same type as y
    """
    assert isinstance(x) == float or int
    assert isinstance(x) == isinstance(y)
    return x+y

def sub(x,y):
    """
    Returns the difference x-y

    Parameter x: The value to subtract from
    Precondition: x is a number

    Parameter y: The value to subtract
    Precondition: y is a number
    """
    assert isinstance(x) == float or int
    return x-y

def remove(s1,s2):
    """
    Returns a copy of s, with all characters in s2 removed.

    Examples:
        remove('abc','ab') returns 'c'
        remove('abc','xy') returns 'abc'
        remove('hello world','ol') returns 'he wrd'

    Parameter s1: the string to copy
    Precondition: s1 is a string

    Parameter s2: the characters to remove
    Precondition: s2 is a string
    """
    assert isinstance(s1) == str
    assert isinstance(s2) == str
    result = ''
    for x in s1:
        if not x in s2:
            result = result + x
    return result

def fold_left(f,seq,value):
    """
    Returns the result of folding f left over seq, starting with value.

    To fold a function f from the left, we
    * Start with value in the accumulator
    * Iterate over the sequence normally
    * At each step, apply f to the accumulator and the next element
    * After applying f, make the new value the accumulator

    Example: Suppose f is - (subtraction), seq is (1,2,3,4) and value is 0.  Then
    the result is

        ((((0-1)-2)-3)-4) = -10

    Parameter f: the function to fold
    Precondition: f is a function that takes two arguments of the same type, and
    returning a value of the same type

    Parameter seq: the sequence to fold
    Precondition: seq is a sequence (tuple, string, etc.) whose elements are the
    same type as that returned by f

    Parameter value: the initial starting value
    Precondition: value has the same type as the return type of f
    """
    assert f == add(x, y) or sub(x, y) or remove(s1, s2)
    assert isinstance(seq) == str or list or tuple
    assert isinstance(value) == int or float

    """
    pseudocode
    append value to seq[0] | diffrent for each type for seq
    for x in seq | apply f | x += 1 | till seq[-1]
    y = seq[0] + 1
    """

    if isinstance(seq) == str:
        seq2 = seq[:0] + value + seq[0:]

    if isinstance(seq) == list:
        seq2 = seq.insert(0, value)

    if isinstance(seq) == tuple:
        seq2 = seq[:0] + (value,) + seq[0:]

    for x in seq2:
        if x != seq2[-1]:
            # var = x += 1
    return
    # pass

def fold_right(f,seq,value):
    """
    Returns the result of folding f right over seq, starting with value.

    To fold a function f from the right, we
    * Start with value in the accumulator
    * Iterate over the sequence right-to-left
    * At each step, apply f to the next element and the accumulator
    * After applying f, make the new value the accumulator

    Example: Suppose f is - (subtraction), seq is (1,2,3,4) and value is 0.  Then
    the result is

        (1-(2-(3-(4-0)))) = -2

    Parameter f: the function to fold
    Precondition: f is a function that takes two arguments of the same type, and
    returning a value of the same type

    Parameter seq: the sequence to fold
    Precondition: seq is a sequence (tuple, string, etc.) whose elements are the
    same type as that returned by f

    Parameter value: the initial starting value
    Precondition: value has the same type as the return type of f
    """
    pass

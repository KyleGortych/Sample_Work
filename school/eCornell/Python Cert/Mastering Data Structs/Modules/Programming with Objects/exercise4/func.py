"""
func
Descript:


File name:  func.py
Maintainer: Kyle Gortych
created:    04-17-2022
"""
def replace_first(tup,a,b):
    """
    Returns a copy of tup with the first occurrence of a replaced by b

    Examples:
        replace_first((1,2,1),1,3) returns (3,2,1)
        replace_first((1,2,1),4,3) returns (1,2,1)

    Parameter tup: The tuple to copy
    Precondition: tup is a tuple of integers

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """
    assert isinstance(tup, tuple)
    assert isinstance(a, int)
    assert isinstance(b, int)

    l = list(tup)
    try:
        var = l.index(a)
        l[var] = b
    except:
        pass

    result = tuple(l)

    return result
    #pass

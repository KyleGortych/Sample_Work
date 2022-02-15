"""
A module to return second item in list

Maintianer: Kyle Gortych
Date:       01-29-2022
"""
import introcs

def second_in_list(s):
    """
    Returns: the second item in comma-separated list

    The final result should not have any whitespace around the edges.

    Example: second_in_list('apple, banana, orange') returns 'banana'
    Example: second_in_list('  do  ,  re  ,  me  ,  fa  ') returns 're'
    Example: second_in_list('z,y,x,w') returns 'y'

    Parameter s: The list of items
    Precondition: s is a string of at least three items separated by commas.
    """
    assert type(s) == str, "The value " + repr(s) + " is not a string."
    assert introcs.count_str(s, ',') >= 2, "The string " + repr(s) + " does not have enough commas."

    pos1 = introcs.find_str(s, ',')
    print(pos1)

    pos2 = introcs.find_str(s, ',', start=pos1 + 1)
    print(pos2)

    slice = s[pos1 + 1:pos2]
    result = introcs.strip(slice)

    return result
    #pass

"""
funcs
Descript:


File name:  funcs.py
Maintainer: Kyle Gortych
created:    04-17-2022
"""
def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Examples:
      first_in_parens('A (B) C') returns 'B'
      first_in_parens('A (B) (C)') returns 'B'
      first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    assert type(s) == str
    assert ('(' in s) and (')' in s)

    pos1 = s.find('(')
    pos2 = s.find(')', pos1 + 1)

    return s[pos1 + 1:pos2]
    # pass


def isnetid(s):
    """
    Returns True if s is a valid Cornell netid.

    Cornell network ids consist of 2 or 3 lower-case initials followed by a
    sequence of digits.

    Examples:
      isnetid('wmw2') returns True
      isnetid('2wmw') returns False
      isnetid('ww2345') returns True
      isnetid('w2345') returns False
      isnetid('WW345') returns False

    Parameter s: the string to check
    Precondition: s is a string
    """
    assert type(s) == str

    var1 = s[:2]
    var2 = s[2:]
    var3 = s[:3]
    var4 = s[3:]

    result = ((var1.isalpha() and var1.islower() and var2.isnumeric() and
        ('-' not in s)) or (var3.isalpha() and var3.islower() and
        var4.isnumeric() and ('-' not in s)))

    return result
    #pass

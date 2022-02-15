"""
The functions for the course project.

Author: Kyle Gortych
Date:   02/08/2022
"""
import introcs

def matching_parens(s):
    """
    Returns True if the string s has a matching pair of parentheses.

    A matching pair pair of parentheses is an open parens '(' followed by a closing
    parens ')'.  Any thing can be between the two pair (including other parens).

    Example: matching_parens('A (B) C') returns True
    Example: matching_parens('A )B( C') returns False

    Parameter s: The string to check
    Precondition: s is a string (possibly empty)
    """
    # Search for the first open parens '('
    # Search for the first close parens ')' AFTER the open parens
    # Compare both searches to -1 and return True if BOTH are not -1
    assert type(s) == str
    pos1 = introcs.find_str(s, '(')
    pos2 = introcs.find_str(s, ')', start=pos1)

    result = pos1 and pos2 != -1
    return result


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Example: first_in_parens('A (B) C') returns 'B'
    Example: first_in_parens('A (B) (C)') returns 'B'
    Example: first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    assert type(s) == str
    pos1 = introcs.find_str(s, '(')
    pos2 = introcs.find_str(s, ')', start=pos1)
    assert (pos1 == -1 or pos2 == -1) == False
    
    result = s[pos1 + 1:pos2]
    return result

"""
A module to print initials of a name

Maintainer: Kyle Gortych
Date:       01-28-2022
"""

import introcs

def initials(n):
    """
    Returns: The initials <first>. <last>. of the given name.

    We assume that n is just two names (first and last). Middle names are
    not supported.

    Example: initials('John Smith') returns 'J. S.'
    Example: initials('Walker White') returns 'W. W.'

    Parameter n: the person's name
    Precondition: n is in the form 'first-name last-name' with one space between names.
    There are no spaces in either <first-name> or <last-name>
    """
    # Find the first initial (and assign it to 'first')
    first = n[0:1]
    print(first)

    # Find the position of the last name (and assign it to 'pos')
    pos = introcs.find_str(n,' ') + 1
    print(pos)

    # Find the last initial (and assign it to 'last')
    last = n[pos]
    print(last)

    # Compute the final answer (and assign it to 'result')
    result = first + '. ' + last + '.'

    # Return the answer
    return result


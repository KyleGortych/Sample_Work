"""
The test script for the course project.

Author: Kyle Gortych
Date:   02/08/2022
"""
import introcs
import funcs

def test_matching_parens():
    """
    Test procedure for matching_parens
    """
    print('Testing matching_parens')

    # Test case 1
    result = funcs.matching_parens('A (B) C')
    introcs.assert_equals(True,result)

    # Test case 2
    result = funcs.matching_parens('A )B( C')
    introcs.assert_equals(False,result)

    # Test case 3
    result = funcs.matching_parens('(')
    introcs.assert_equals(False,result)

    # Test case 4
    result = funcs.matching_parens(')')
    introcs.assert_equals(False,result)

    # Test case 5
    result = funcs.matching_parens('A')
    introcs.assert_equals(False,result)

    # Test case 6
    result = funcs.matching_parens('(()')
    introcs.assert_equals(True,result)

    # Test case 7
    result = funcs.matching_parens('(())')
    introcs.assert_equals(True,result)


def test_first_in_parens():
    """
    Test procedure for first_in_parens
    """
    print('Testing first_in_parens')

    # Test case 1
    result = funcs.first_in_parens('A (B) C')
    introcs.assert_equals('B',result)

    # Test case 2
    result = funcs.first_in_parens('A (B) (C)')
    introcs.assert_equals('B',result)

    # Test case 3
    result = funcs.first_in_parens('A ((B) (C))')
    introcs.assert_equals('(B',result)

    # Test case 4
    result = funcs.first_in_parens('(()')
    introcs.assert_equals('(',result)

    # Test case 5
    result = funcs.first_in_parens('()')
    introcs.assert_equals('',result)

# Script Code
test_matching_parens()
test_first_in_parens()

print('Module funcs is working correctly')

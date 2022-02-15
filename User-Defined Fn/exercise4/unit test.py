"""
A test script to test the module func.py

Author: Kyle Gortych
Date:  01-26-2022
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing


def test_replace_first():
    """
    Test procedure for replace_first
    """
    print('Testing replace_first')

    # Put your tests below this line

    # test case 1
    result = funcs.replace_first('crane', 'a', 'o')
    introcs.assert_equals('crone', result)

    # test case 2
    result = funcs.replace_first('poll', 'l', 'o')
    introcs.assert_equals('pool', result)

    # test case 3
    result = funcs.replace_first('crane', 'cr', 'b')
    introcs.assert_equals('bane', result)

# Script Code
# Do not write below this line
test_replace_first()
print('Module funcs is working correctly')


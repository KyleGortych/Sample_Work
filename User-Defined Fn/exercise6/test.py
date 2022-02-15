"""
A test script to verify the function second_in_list.

This script is complete.  You do not need to modify it.

Author: Kyle Gortych
Date:   01-29-2022
"""
import introcs
import func_slice


def test_second_in_list():
    """
    Test procedure for second_in_list.
    """
    print('Testing second_in_list')

    # Should work after steps 1 and 2
    result = func_slice.second_in_list('apple, banana, orange')
    introcs.assert_equals('banana',result)

    # Should work after step 3
    result = func_slice.second_in_list('Billy, Andrew, Wendy')
    introcs.assert_equals('Andrew',result)

    result = func_slice.second_in_list('apple,   fig , orange')
    introcs.assert_equals('fig',result)

    # Should work after step 4
    result = func_slice.second_in_list('apple, fig, banana')
    introcs.assert_equals('fig',result)

    result = func_slice.second_in_list('apple, fig, banana, orange')
    introcs.assert_equals('fig',result)

    # Should work after step 5
    result = func_slice.second_in_list('do  ,  re  ,  me  ,  fa  ')
    introcs.assert_equals('re',result)

    result = func_slice.second_in_list('z,y,x,w')
    introcs.assert_equals('y',result)


# Script Code
# Do not write below this line
test_second_in_list()
print('Module func is working correctly')

"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Kyle Gortych
Date:   02/16/2022
"""
import introcs
import currency

def test_before_space():
    """Test procedure for before_space"""
    print('Testing before_space')

    # Test case 1
    s = currency.before_space('Hello World')
    introcs.assert_equals('Hello',s)

    # Test case 2
    s = currency.before_space('H ello World')
    introcs.assert_equals('H',s)

    # Test case 3
    s = currency.before_space(' HelloWorld')
    introcs.assert_equals('',s)

    # Test case 4
    s = currency.before_space('Hel   World')
    introcs.assert_equals('Hel',s)


def test_after_space():
    """Test procedure for after_space"""
    print('Testing after_space')

    # Test case 1
    s = currency.after_space('Hello World')
    introcs.assert_equals('World',s)

    # Test case 2
    s = currency.after_space(' Hello World')
    introcs.assert_equals('Hello World',s)

    # Test case 3
    s = currency.after_space('HelloWorld ')
    introcs.assert_equals('',s)

    # Test case 4
    s = currency.after_space('Hello  World')
    introcs.assert_equals(' World',s)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print('Testing first_inside_quotes')

    # Test case 1
    s = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C',s)

    # Test case 2
    s = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C',s)

    # Test case 3
    s = currency.first_inside_quotes('A "" ')
    introcs.assert_equals('',s)

    # Test case 4
    s = currency.first_inside_quotes('" "')
    introcs.assert_equals(' ',s)


def test_get_src():
    """Test procedure for get_src"""
    print('Testing get_src')

    # Test case 1
    s = currency.get_src('{"success": true, "src": "2 United States Dollars", '
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',s)

    # Test case 2
    s = currency.get_src('{"success":false,"src":"","dst":"",'
    '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',s)

    # Test case 3
    s = currency.get_src('{"success":true, "src":"2 United States Dollars", '
    '"dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars',s)

    # Test case 4
    s = currency.get_src('{"success":false,"src":  "","dst":"","error":'
    '"Source currency code is invalid."}')
    introcs.assert_equals('',s)


def test_get_dst():
    """Test procedure for get_dst"""
    print('Testing get_dst')

    # Test case 1
    s = currency.get_dst('{"success": true, "src": "2 United States Dollars", '
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',s)

    # Test case 2
    s = currency.get_dst('{"success":false,"src":"","dst":"",'
    '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',s)

    # Test case 3
    s = currency.get_dst('{"success":true, "src":"2 United States Dollars", '
    '"dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros',s)

    # Test case 4
    s = currency.get_dst('{"success":false,"src":  "","dst": "",'
    '"error":"Source currency code is invalid."}')
    introcs.assert_equals('',s)


def test_has_error():
    """Test procedure for has_error"""
    print('Testing has_error')

    # Test case 1
    s = currency.has_error('{"success": true, "src": "2 United States Dollars", '
    '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(s)

    # Test case 2
    s = currency.has_error('{"success":false,"src":"","dst":"",'
    '"error":"Source currency code is invalid."}')
    introcs.assert_true(s)

    # Test case 3
    s = currency.has_error('{"success":true, "src":"2 United States Dollars", '
    '"dst":"1.772814 Euros", "error":""}')
    introcs.assert_false(s)

    # Test case 4
    s = currency.has_error('{"success": false,"src":  "","dst": "","error": '
    '"Source currency code is invalid."}')
    introcs.assert_true(s)


def test_service_response():
    """Test procedure for service_response"""
    print('Testing service_response')

    # Test case 1
    s = currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", '
    '"dst": "2.2160175 Euros", "error": ""}',s)

    # Test case 2
    s = currency.service_response('Dollars','EUR',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": '
    '"The rate for currency DOLLARS is not present."}',s)

    # Test case 3
    s = currency.service_response('USD','Euros',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": '
    '"The rate for currency EUROS is not present."}',s)

    # Test case 4
    s = currency.service_response('USD','EUR',-2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 United States Dollars", '
    '"dst": "-2.2160175 Euros", "error": ""}',s)


def test_iscurrency():
    """Test procedure for iscurrency"""
    print('Testing iscurrency')

    # Test case 1
    s = currency.iscurrency('USD')
    introcs.assert_equals(True,s)

    # Test case 2
    s = currency.iscurrency('TIM')
    introcs.assert_false(s)


def test_exchange():
    """Test procedure for exchange"""
    print('Testing exchange')

    # Test case 1
    s = currency.exchange('USD','EUR',2.5)
    introcs.assert_floats_equal(2.2160175,s)

    # Test case 2
    s = currency.exchange('USD','EUR',-2.5)
    introcs.assert_floats_equal(-2.2160175,s)


# fn calls
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print('All tests completed successfully.')

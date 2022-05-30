"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Kyle Gortych
Date:   02/16/2022
"""
import introcs

APIKEY = "omitted"

def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    a = introcs.find_str(s,' ')
    s = s[0:a]

    assert a != -1, 'if value of a is -1 then no space was in the str array'

    return s
    #pass


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    a = introcs.find_str(s,' ')
    s = s[a+1:]

    assert a >= 0

    return s
    # pass


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    a = introcs.find_str(s,'"')
    assert a >= 0
    a = a+1 # a is the index of the first letter after the first "

    a1 = introcs.find_str(s[a:],'"')
    assert a1 >= 0
    a1 = a1+a # a1 is the index of the last letter before the next "

    s = s[a:a1]

    return s
    # pass


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str
    s1 = introcs.split(json,'"')
    json = s1[5]
    json = introcs.strip(json,'"')

    # print(json)
    return json
    # pass


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str
    s1 = introcs.split(json,'"')
    json = s1[9]
    json = introcs.strip(json,'"')

    # print(json)
    return json
    # pass


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    assert type(json) == str
    pos1 = introcs.find_str(json,':')
    pos2 = introcs.find_str(json,',')
    json = json[pos1+1:pos2]
    json = introcs.strip(json)

    result = (json == 'true' == False) or (json == 'false')

    return result
    #pass


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    # https://ecpyfac.ecornell.com/python/currency/fixed?src=USD&dst=EUR&amt=2.5&key=

    global APIKEY
    assert (type(src) == str) and (type(dst) == str), 'Data type not an str'
    assert (introcs.isalpha(src) == True) and (introcs.isalpha(dst) == True)
    assert ((type(amt) == int) or (type(amt) == float)), 'Data type not an int or float'
    assert len(src) and len(dst) > 0, 'Precondition nonempty str'
    amt_str = str(amt)

    s = 'https://ecpyfac.ecornell.com/python/currency/fixed?src=' + src + '&dst'\
    '=' + dst + '&amt=' + amt_str + '&key=' + APIKEY

    introcs.strip(s)
    #print(s)
    result = introcs.urlread(s)

    return result
    #pass


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert type(currency) == str
    assert introcs.isalpha(currency) == True

    src = currency
    dst = 'EUR'
    amt = 2.5

    var1 = service_response(src, dst, amt)
    result = has_error(var1) == False
    #print(src)
    #print(dst)
    #print(amt)
    #print(var1)
    return result
    #pass


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    full_str = service_response(src,dst,amt)
    assert has_error(full_str) == False
    sub_str = get_dst(full_str)
    sub_str2 = before_space(sub_str)

    result = float(sub_str2) or int(sub_str2)

    return result
    #pass

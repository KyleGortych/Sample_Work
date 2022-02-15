"""
A function with several helpers.

The primary function in this module is str_to_seconds.  The functions get_hours, 
get_minutes, and get_seconds are all helper functions that are used to implement 
this function.  They should implemented in the order listed.

Author: Kyle Gortych
Date: 1/30/2022
"""
import introcs


def iso_8601(s):
    """
    Returns True if s is a string in ISO 8601 format, False otherwise
    
    Parameter time: The string to check
    Precondition: s is a string of length 8
    """
    colon_pos1 = introcs.find_str(s, ':')
    #print(colon_pos1)

    colon_pos2 = introcs.rfind_str(s, ':')
    #print(colon_pos2)

    # This is a hint to get you started
    # Create variable to check if the first two characters are digits
    #check1 = introcs.isdigit(s[:2]) and introcs.isdigit(s[2+1:5]) and introcs.isdigit(s[5+1:]) == True
    #assert introcs.isdigit(s[:2]) and introcs.isdigit(s[2+1:5]) and introcs.isdigit(s[5+1:]) == True
    #print(introcs.isdigit(s[2+1:5]))
    #print(introcs.isdigit(s[5+1:]))

    # Create variable to check if third character is a colon
    #check2 = s[2] == ':'
    #assert s[2] == ':'

    #check3 = len(s) == 8
    #assert len(s) == 8

    #check4 = len(s[:colon_pos1]) and len(s[colon_pos1:colon_pos2 - 1]) and len(s[colon_pos2 + 1:]) <= 2 
    #assert len(s[:colon_pos1]) and len(s[colon_pos1:colon_pos2 - 1]) and len(s[colon_pos2 + 1:]) <= 2 
    #print(len(s[:colon_pos1]))
    #print(len(s[colon_pos1:colon_pos2 - 1]))
    #print(len(s[colon_pos2 + 1:]))
    # FINISH THIS FUNCTION
    check1 = introcs.isdigit(s[:2]) and introcs.isdigit(s[2+1:5]) and introcs.isdigit(s[5+1:]) == True
    check2 = s[2] == ':'
    check3 = len(s) == 8
    check4 = len(s[:colon_pos1]) and len(s[colon_pos1:colon_pos2 - 1]) and len(s[colon_pos2 + 1:]) <= 2 
    # Return True if all checks pass
    #return check1 and check2 # AND...
    return check1 and check2 and check3 and check4 == True
    

def get_seconds(time):
    """
    Returns the number of seconds in the string time (as an int).
    
    The value time is a string in extended ISO 8601 format.  That is, it has the form 
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for 
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see
        
        https://en.wikipedia.org/wiki/ISO_8601#Times
    
    This function does not support time zones, abbreviated formats, or decimals
    
    Example: get_seconds('12:35:15') returns 15
    Example: get_seconds('03:02:05') returns 5
    Example: get_seconds('00:00:00') returns 0
    
    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str 
    assert len(time) == 8
    assert iso_8601(time) == True
    sec = time[6:]
    result = int(sec)
    return result


def get_minutes(time):
    """
    Returns the number of minutes in the string time (as an int).
    
    The value time is a string in extended ISO 8601 format.  That is, it has the form 
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for 
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see
        
        https://en.wikipedia.org/wiki/ISO_8601#Times
    
    This function does not support time zones, abbreviated formats, or decimals
    
    Example: get_minutes('12:35:15') returns 35
    Example: get_minutes('03:02:05') returns 2
    Example: get_minutes('00:00:00') returns 0
    
    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str 
    assert len(time) == 8
    assert iso_8601(time) == True
    min = time[3:5]
    result = int(min)
    return result

def get_hours(time):
    """
    Returns the number of hours in the string time (as an int).
    
    The value time is a string in extended ISO 8601 format.  That is, it has the form 
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for 
    hours, minutes, and seconds, so they are padded with 0s when necessary.
    leading 0s if they are only one digit, but there may be only one hour digit. For
    more information, see
        
        https://en.wikipedia.org/wiki/ISO_8601#Times
    
    This function does not support time zones, abbreviated formats, or decimals
    
    Example: get_hours('12:35:15') returns 12
    Example: get_hours('03:02:05') returns 3
    Example: get_hours('00:00:00') returns 0
    
    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str 
    assert len(time) == 8
    assert iso_8601(time) == True
    hr = time[0:2]
    result = int(hr)
    return result

def str_to_seconds(time):
    """
    Returns the number of seconds since midnight in the string time (as an int).
    
    The value time is a string in extended ISO 8601 format.  That is, it has the form 
    'hh:mm:ss' where h, m, and s are digits.  There must be exactly two digits each for 
    hours, minutes, and seconds, so they are padded with 0s when necessary.  So 
    seconds, minutes, and hours may have leading 0s if they are only one digit. For
    more information, see
        
        https://en.wikipedia.org/wiki/ISO_8601#Times
    
    This function does not support time zones, abbreviated formats, or decimals
    
    Example: str_to_seconds('12:35:15') returns 45315
    Example: str_to_seconds('03:02:05') returns 10925
    Example: str_to_seconds('00:00:00') returns 0
    
    Parameter time: The string representation of the time
    Precondition: time is a string in extended ISO 8601 format 'hh:mm:ss'
    """
    assert type(time) == str 
    assert len(time) == 8
    assert iso_8601(time) == True
    
    result = get_hours(time)*60*60 + get_minutes(time)*60 + get_seconds(time)
    return result
    
    # assert iso_8601(time) == True | works but not whats needed
    # assert type(time[get_hours(time):get_seconds(time)]) == str | works but not whats needed 
    # ¬ assert time == str
    # change params in fn from time to hr, min, sec | str concatination?
    
    #assert introcs.isdigit(time[0:1+1]) and introcs.isdigit(time[3:4+1]) and introcs.isdigit(time[6:7+1]) == True
    #assert type(time[get_hours(time):get_seconds(time)]) == str 
    
    #print(time[0:1+1], time[3:4+1], time[6:7+1])

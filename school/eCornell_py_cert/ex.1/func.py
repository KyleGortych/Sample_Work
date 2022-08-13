"""
A simple function comparing datetime objects.

Author: Kyle Gortych
Date:   08-13-2022
"""
import datetime

def is_before(d1,d2):
    """
    Returns True if event d1 happens before d2.

    Values d1 and d2 can EITHER be date objects or datetime objects.
    If a date object, assume that it happens at midnight of that day.

    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object

    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison
    assert isinstance(d1, (datetime.datetime, datetime.date))
    assert isinstance(d2, (datetime.datetime, datetime.date))

    if type(d1) == datetime.date and type(d2) != datetime.date:
        if datetime.datetime(d1.year, d1.month, d1.day) < d2:
            return True
        return False

    if type(d1) != datetime.date and type(d2) == datetime.date:
        if d1 < datetime.datetime(d2.year, d2.month, d2.day):
            return True
        return False

    if d1 < d2:
        return True
    return False
    #pass

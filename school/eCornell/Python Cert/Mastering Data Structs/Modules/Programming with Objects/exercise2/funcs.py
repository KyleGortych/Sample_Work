"""
funcs
Descript:


File name:  funcs.py
Maintainer: Kyle Gortych
created:    04-08-2022
"""
import clock


def add_time1(time1, time2):
    """
    Returns the sum of time1 and time2 as a new Time object

    DO NOT ALTER time1 or time2, even though they are mutable

    Examples:
        The sum of 12hr 13min and 13hr 12min is 25hr 25min
        The sum of 1hr 59min and 3hr 2min is 5hr 1min

    Parameter time1: the starting time
    Precondition: time1 is a Time object

    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    assert type(time1) == clock.Time
    assert type(time2) == clock.Time

    timehr = time1.hours + time2.hours

    timemin = time1.minutes + time2.minutes
    if timemin >= 60:
        timehr = (timemin // 60) + timehr
        timemin = (timemin % 60)

    total = clock.Time(timehr,timemin)

    return total
    #pass


def add_time2(time1, time2):
    """
    Modifies time1 to be the sum of time1 and time2

    DO NOT RETURN a new time object.  Modify the object time1 instead.

    Examples:
        The sum of 12hr 13min and 13hr 12min is 25hr 25min
        The sum of 1hr 59min and 3hr 2min is 5hr 1min

    Parameter time1: the starting time
    Precondition: time1 is a Time object

    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    assert type(time1) == clock.Time
    assert type(time2) == clock.Time

    timehr = time1.hours + time2.hours

    timemin = time1.minutes + time2.minutes
    if timemin >= 60:
        time1.hours = (timemin // 60) + timehr
        time1.minutes = (timemin % 60)
    else:
        time1.hours = timehr
        time1.minutes = timemin

    # time1 = clock.Time(timehr,timemin)
    # print(time1)
    #pass

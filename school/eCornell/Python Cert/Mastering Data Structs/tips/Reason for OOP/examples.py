"""
examples
Descript:
Reasons why primitive types are problematic
and why we need objects.

File name:     examples.py
Maintainer:    Kyle Gortych
Created:       05-25-2022
Last Modified: xx-xx-xxxx
"""
import math
from introcs import Point3

def distance1(x0,y0,z0,x1,y1,z1):
    """
    return: The distance between two points (x0,y0,z0) and (x1,y1,z1)

    parameter x0: The x-coordinate for the first point
    precondition x0: is a float

    parameter y0: The y-coordinate for the first point
    precondition y0: is a float
    etc...
    """
    # assert etc...

def distance2(p0, p1):
    """
    return: The distance between two points p0 and p1

    parameter p0: The first point
    precondition p0: Consists of three floats

    parameter p1: The second point
    precondition p1: Consists of three floats
    """
    assert isinstance(p0) == tuple, repr(p0) + 'is not a tuple'
    assert len(p0) == 3, repr(p0) + 'has the incorrect length'
    assert isinstance(p0[0]) == float, repr(p0) + 'is not a float'
    assert isinstance(p0[1]) == float, repr(p0) + 'is not a float'
    assert isinstance(p0[2]) == float, repr(p0) + 'is not a float'
    assert isinstance(p1) == tuple, repr(p1) + 'is not a tuple'
    assert len(p1) == 3, repr(p1) + 'has the incorrect length'
    assert isinstance(p1[0]) == float, repr(p1) + 'is not a float'
    assert isinstance(p1[1]) == float, repr(p1) + 'is not a float'
    assert isinstance(p1[2]) == float, repr(p1) + 'is not a float'

    d2x = (p0[0]-p1[0]) * (p0[0]-p1[0])
    d2y = (p0[1]-p1[1]) * (p0[1]-p1[1])
    d2z = (p0[2]-p1[2]) * (p0[2]-p1[2])

    return math.sqrt(d2x + d2y + d2z)

def distance3(p0,p1):
    """
    return: The distance between two points p0 and p1

    parameter p0: The first point
    precondition p0: Consists of three floats

    parameter p1: The second point
    precondition p1: Consists of three floats
    """
    assert isinstance(p0) == Point3, repr(p0) + 'is not a Point3 object'
    assert isinstance(p1) == Point3, repr(p1) + 'is not a Point3 object'

    d2x = (p0[0]-p1[0]) * (p0[0]-p1[0])
    d2y = (p0[1]-p1[1]) * (p0[1]-p1[1])
    d2z = (p0[2]-p1[2]) * (p0[2]-p1[2])

    return math.sqrt(d2x + d2y + d2z)

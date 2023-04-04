#!/usr/bin/python3
"""
This is an integer addition module.

It has one fuction, add_integer().
"""


def add_integer(a, b=98):
    """Return the addition of a and b.
    Float args are casted into integers before addition
    Raises:
        TypeError: If a or b is a non-integer or non-float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

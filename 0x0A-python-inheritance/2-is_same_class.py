#!/usr/bin/python3
"""has a function that checks if the object is an instance of the class."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of the class.

    Args:
        obj : object we want to check
        a_class : the class we want to check the object from

    Returns:
        returns True if it matches and False if it doesn't
    """
    return (type(obj) == a_class)

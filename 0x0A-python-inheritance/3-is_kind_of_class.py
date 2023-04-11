#!/usr/bin/python3
"""has a is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """check if an obj is an instance or inherited instance of class.

    Args:
        obj : object we want to check
        a_class : the class we want to check the object from

    Returns:
         returns True if it matches and False if it doesn't
    """
    return (isinstance(obj, a_class)) 

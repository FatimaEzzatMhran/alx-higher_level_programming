#!/usr/bin/python3
"""Contains a function that adds attributes."""


def add_attribute(obj, attribute, value):
    """Add a new attribute.

    Args:
        obj : the object to add an attribute to
        attribute : The name of the attribute you want to set
        value : The value you want to give the specified attribute
    Raises:
        TypeError: if the object can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)

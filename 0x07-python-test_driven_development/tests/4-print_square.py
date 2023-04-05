#!/usr/bin/python
"""
This is the print square module.

This module has one function that prints a square using '#'.
"""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): width and height of the square.
    Raises:
        TypeError: If size provided is not an integer
        ValueError: If size provided is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print('#' * int(size))

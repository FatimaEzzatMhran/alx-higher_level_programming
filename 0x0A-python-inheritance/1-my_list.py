#!/usr/bin/python3
"""This module has MyList class which has one function."""


class MyList(list):
    """subclass of list."""
    def __init__(self):
        """initialize object."""
        super().__init__()

    def print_sorted(self):
        """prints sorted list."""
        print(sorted(self))

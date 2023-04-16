#!/usr/bin/python
"""This module contains a class named ``Base``."""


class Base:
    """
    class Base: will be the base of all other classes in this project.
    goal: is to manage id attribute in all future classes.
    why: to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization method for Base."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

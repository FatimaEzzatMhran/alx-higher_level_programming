#!/usr/bin/python3
"""
This is the "1-rectangle" module.

It provides a rectangle class with attributes: width and height.
"""


class Rectangle:
    """Rectangle class with attributes: width and height."""

    def __init__(self, width=0, height=0):
        """Initialization of a new Rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for private instance attribute width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

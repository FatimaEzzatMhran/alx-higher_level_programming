#!/usr/bin/python3
"""Contains the class BaseGeometry and subclass Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the print() and str() of the rectangle."""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

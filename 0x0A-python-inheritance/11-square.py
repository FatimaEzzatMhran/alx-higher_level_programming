#!/usr/bin/python3
"""Contains the class Rectangle and the subclass Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """square Initialization.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square."""
        return (self.__size * self.__size)

    def __str__(self):
        """Return the print() and str() of the rectangle."""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))

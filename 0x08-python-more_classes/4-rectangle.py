#!/usr/bin/python3
"""
This is the "2-rectangle" module.

It provides a rectangle class with attributes: width and height.
And it provideds methods to calculate area and perimiter.
"""


class Rectangle:
    """Rectangle class with attributes: width and height, and
    methods to calculate area, perimiter, print, str.
    """

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

    def area(self):
        """returns the area of a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns printable string representation of a rectangle.

        The rectangle is represented with # character.
        """
        rectan = ""
        if self.__width == 0 or self.__height == 0:
            return rectan
        for i in range(self.__height):
            rectan += ("#" * self.__width)
            if i != self.__height - 1:
                rectan += "\n"
        return rectan

    def __repr__(self):
        """return a string representation of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

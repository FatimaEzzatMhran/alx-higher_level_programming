#!/usr/bin/python3
"""This module contains a Rectangle class that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of a new Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # getter functions
    @property
    def width(self):
        """Get the value of the rectangle width."""
        return self.__width

    @property
    def height(self):
        """Get the value of the rectangle height."""
        return self.__height

    @property
    def x(self):
        """Get the value of the rectangle x."""
        return self.__x

    @property
    def y(self):
        """Get the value of the rectangle y."""
        return self.__y

    # setter functions
    @width.setter
    def width(self, value):
        """Set the value of the rectangle width."""
        if (type(value) != int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Set the value of the rectangle height."""
        if (type(value) != int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Set the value of the rectangle x."""
        if (type(value) != int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Set the value of the rectangle y."""
        if (type(value) != int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

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

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def display(self):
        """prints the rectangle presented with # char."""
        if self.__width == 0 or self.__height == 0:
            print("")
            return

        for y in range(self.y):
            print("")
        for i in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """return a string representation of the rectangle."""
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                    self.__x, self.__y,
                                           self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute.
        *args: new values for the attribute
                1st argument should be the id attribute.
                2nd argument should be the width attribute.
                3rd argument should be the height attribute.
                4th argument should be the x attribute.
                5th argument should be the y attribute.
        **kwargs: assigns a key/value args to attributes.
        """
        if args and len(args) != 0:
            f = 0
            for arg in args:
                if f == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif f == 1:
                    self.width = arg
                elif f == 2:
                    self.height = arg
                elif f == 3:
                    self.x = arg
                elif f == 4:
                    self.y = arg
                f += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

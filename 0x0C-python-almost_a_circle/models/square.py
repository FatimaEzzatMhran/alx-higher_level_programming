#!/usr/bin/python3
"""This module contains a Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of a new square."""
        super().__init__(size, size, x, y, id)

    # getter method
    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    # setter method
    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if (type(value) != int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """return a string representation of the square."""
        return "[Square] ({}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.height)

    def update(self, *args, **kwargs):
        """assigns an arg to each attr(updates attr of an instance.
        *args: new values for the attr.
                1st argument should be the id attribute.
                2nd argument should be the size attribute.
                3rd argument should be the x attribute.
                4th argument should be the y attribute.
        **kwargs: assigns a key/value args to attributes.
        """
        if args and len(args) != 0:
            f = 0
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
            for arg in args:
                if f == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif f == 1:
                    self.size = arg
                elif f == 2:
                    self.x = arg
                elif f == 3:
                    self.y = arg
                f += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square."""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}

#!/usr/bin/python3
"""
This is the "8-rectangle" module.

It provides a rectangle class with attributes: width and height.
And it provideds methods to calculate area and perimiter.
"""


class Rectangle:
    """Rectangle class with attributes: width and height, and
    methods to calculate area, perimiter, print, str, repr, del.

    Attributes:
    number_of_instances(int): class attr keeps track of num of instances.
    print_symbol(any type): Used as symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of a new Rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        for i in range(self.__height):
            for j in range(self.__width):
                try:
                    rectan += str(self.print_symbol)
                except Exception:
                    rectan += type(self).print_symbol
            if i != self.__height - 1:
                rectan += "\n"
        return rectan

    def __repr__(self):
        """return a string representation of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print a message when an instance of a rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area.

        Args:
            rect_1(Rectangle): 1st rectangle.
            rect_2(Rectangle): 2nd rectangle.
        Raise:
            TypeError: If one of the args is not a rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        

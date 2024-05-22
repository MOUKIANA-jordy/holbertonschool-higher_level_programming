#!/usr/bin/python3
"""
    File for the class Rectangle.
"""


class Rectangle:
    """
        Class that defines a rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            Initialization of the Rectangle class.
            Arguments:
                width (int, optional): Width of the rectangle.
                height (int, optional): Height of the rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            Get the width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter of the width of a rectangle.
            Arguments:
                value (int): Value to add.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Get the height of a rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter of the height of a rectangle.
            Arguments:
                value (int): Value to add.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Returns the rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """
            Returns the rectangle perimeter.
        """
        width = self.width
        height = self.height
        if width == 0 or height == 0:
            return 0
        return (width + height) * 2

    def __str__(self):
        text = ""
        if self.height != 0 and self.width != 0:
            for i in range(self.height):
                text += "{:s}{:s}".format(
                    self.width * "#",
                    "" if (i + 1) == self.height else "\n"
                )
        return text

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

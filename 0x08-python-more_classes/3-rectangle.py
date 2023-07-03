#!/usr/bin/python3
"""class that defines and draw a square"""


class Rectangle:
    """ Class beginning"""

    def __init__(self, width, height):
        """Initialzing the attributes"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """attributes the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width to the given value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """attrubutes the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ area of the recrangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """perimeter of a rectangle"""
        return ((2 * self.__height) + (2 * self.__width))

    def __str__(self) -> str:
        """diagram of a rectangle"""
        total = ""
        for _ in range(self.__height):
            for x in range(self.__width):
                total += "#"
            if _ < (self.__height - 1):
                total += "\n"
        return total

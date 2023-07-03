#!/usr/bin/python3
"""creation of class that a rectangle"""


class Rectangle:
    """ Declaration of the class and its attributes"""

    def __init__(self, width, height):
        """Initializing the rectangke class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError if the variale is not an integer
            ValueError if the variable is less than zero
            """

        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width attribute tk the vakue given"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height attribute to the value given"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return ((2 * self.__width) + (2 * self.__height))

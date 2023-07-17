#!/usr/bin/python3

from models.base import Base
"""Defining the base method"""


class Rectangle(Base):
    """Creating the class named Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Setting the width method"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width method"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Display method"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + self.width * "#")

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """Update method"""
        list_ = ["id", "width", "height", "x", "y"]

        if args is not None and bool(args) is True:
            x = 0
            for _ in list_:
                try:
                    """args[x] = list_[x]"""
                    setattr(self, _, args[x])

                except IndexError:
                    pass
                x += 1
        else:
            for _ in list_:
                try:
                    setattr(self, _, kwargs[_])
                except KeyError:
                    pass

    def to_dictionary(self):
        """To dictionary method"""
        list_ = ["x", "y", "id", "height", "width"]
        list_dict = {}
        for _ in list_:
            list_dict[_] = getattr(self, _)
        return list_dict

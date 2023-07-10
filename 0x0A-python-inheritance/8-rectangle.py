#!/usr/bin/python3
"""Creation of a rectamgle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The rectangle class created"""

    def __init__(self, width, height):
        """Intialize the rectangle class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

#!/usr/bin/python3
"""Base geometry class"""


class BaseGeometry:
    """Creating the class"""

    def area(self):
        """To check if the parameter is of the the given variable type
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        return ("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3

def add_integer(a, b=98):
    """ Gunction that adds two integers
    Raises:
        Error if one of the given baruabke is not an integer


    """
    if not isinstance(a, int) and not isinstance(a, float):
        """first exemption"""
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

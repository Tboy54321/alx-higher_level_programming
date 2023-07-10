#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """ Args:
    obj (any): The object to check.
    a_class (type): The class to match the type of obj to

    Returns true if an object is a subclass of the specified class
    (directly or indirectly) from the specified class; otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)

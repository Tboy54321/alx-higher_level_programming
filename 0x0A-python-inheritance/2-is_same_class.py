#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Checks if object is an instance of a class,
    Returns true if an objrct is if the same data type"""
    return (type(obj) == a_class)

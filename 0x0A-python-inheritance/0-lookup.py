#!/usr/bin/python3
"""Defines an object attribute and methods using lookup function."""


def lookup(obj):
    """returns a list with objects available attributes"""
    return dir(obj)

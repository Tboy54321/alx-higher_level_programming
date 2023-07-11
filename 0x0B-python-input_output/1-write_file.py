#!/usr/bin/python3
"""Creating a function that writes to a file"""


def write_file(filename="", text=""):
    """Creating the function"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Writing a function that reads a txt file"""


def read_file(filename=""):
    """creating the function"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

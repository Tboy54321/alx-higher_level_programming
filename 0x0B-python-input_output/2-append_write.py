#!/usr/bin/python3
"""Writing a function that creates amd write text to a file"""


def append_write(filename="", text=""):
    """Creating the function"""

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)

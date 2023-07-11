#!/usr/bin/python3
"""Function that creates and save data into the file"""


def load_from_json_file(filename):
    """Creates the function"""
    with open(filename) as file:
        return json.load(file)

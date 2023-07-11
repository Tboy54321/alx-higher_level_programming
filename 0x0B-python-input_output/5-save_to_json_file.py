#!/usr/bin/python3
"""Function that writes a ibject to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file in JSON"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)

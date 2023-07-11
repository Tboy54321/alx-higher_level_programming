#!/usr/bin/python3
"""function that returns an object rep by a json string"""
import json


def from_json_string(my_str):
    """converts the data from strings"""
    return json.loads(my_str)

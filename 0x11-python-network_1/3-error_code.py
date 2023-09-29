#!/usr/bin/python3
"""Python script that takes in a URL"""
"""sends a request to the URL and displays the body of the response"""


import urllib.request
import urllib.error
from sys import argv


def error_code(url):
    """error_code function"""
    response = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(response) as responses:
            print(responses.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    error_code(argv[1])

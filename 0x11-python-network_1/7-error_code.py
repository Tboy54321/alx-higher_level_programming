#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""
import requests
from sys import argv


def error_code(url):
    """error_code function"""
    url_ = url[1]
    request = requests.get(url_)
    if request.status_code == requests.codes.ok:
        print(request.text)
    else:
        print("Error code: {}".format(request.status_code))


if __name__ == "__main__":
    error_code(argv)

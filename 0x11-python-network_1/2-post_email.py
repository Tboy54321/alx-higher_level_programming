#!/usr/bin/python3
"""Python script that takes in a URL and an email"""


import urllib.request
from sys import argv


def email_parameter(argv):
    """email_parameter function"""
    params = {'email': argv[2]}
    data = (urllib.parse.urlencode(params)).encode('utf8')
    url_ = argv[1]
    response = urllib.request.Request(url_, data)
    with urllib.request.urlopen(response) as request:
        response = request.read()
        print(response.decode('utf8'))


if __name__ == "__main__":
    email_parameter(argv)

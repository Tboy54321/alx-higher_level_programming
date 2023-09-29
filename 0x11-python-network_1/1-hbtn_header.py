#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL"""


import urllib.request
from sys import argv


def fetch_header(url):
    """fetch_header class"""
    with urllib.request.urlopen(url) as request:
        response = request.info()
        print(response['X-Request-Id'])


if __name__ == "__main__":
    fetch_header(argv[1])

#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


response = urllib.request.Request("https://alx-intranet.hbtn.io/status")

if __name__ == "__main__":
    with urllib.request.urlopen(response) as responses:
        body = responses.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

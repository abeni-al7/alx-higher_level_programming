#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the body of the response and if the http status
code is greater than or wqual to 400 it prints it as an
error code"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)

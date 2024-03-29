#!/usr/bin/python3
"""This script takes my github credentials(username and
password) and uses the GitHub API to display my id.
It uses Basic Authentication with personal access token
as password. The first argument is my username and the second
argument will be my personal access token as password"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    response = requests.get(url, auth=(username, password))
    try:
        print(response.json()['id'])
    except KeyError:
        print("None")

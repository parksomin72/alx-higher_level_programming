#!/usr/bin/python3
"""
Query GitHub API for user id.
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    user_id = requests.get(
        f'https://api.github.com/users/{argv[1]}',
        auth=HTTPBasicAuth(argv[1], argv[2])
    ).json().get('id')

    print(user_id)

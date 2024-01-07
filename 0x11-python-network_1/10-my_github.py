#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = 'https://api.github.com/user'
auth = (username, token)

try:
    response = requests.get(url, auth=auth)
    data = response.json()
    print(data.get('id'))
except ValueError:
    print(None)

#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL,
and displays the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    # Make the request and get the response
    response = requests.get(url)

    # Check if X-Request-Id is present in the response headers
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id is not None:
        print(x_request_id)
    else:
        print("None")

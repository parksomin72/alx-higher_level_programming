#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request,
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) < 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Make the request and read the response
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))

    except urllib.error.HTTPError as e:
        # Handle HTTPError exceptions
        print("Error code: {}".format(e.code))

#!/usr/bin/python3
"""
This script sends a request to a given URL and displays the value of the X-Request-Id variable in the header of the response.
"""

import urllib.request
import sys


if __name__ == "__main__":
    # Check if URL is provided
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]

    # Send request and display X-Request-Id value
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader("X-Request-Id")
        if x_request_id:
            print(x_request_id)

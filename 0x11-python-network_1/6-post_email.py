#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) < 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Display the email being sent
    print("Your email is: {}".format(email))

    # Make the POST request with the email as a parameter
    payload = {'email': email}
    response = requests.post(url, data=payload)

    # Display the body of the response
    print(response.text)

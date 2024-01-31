#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    # Set the default value for the letter
    q = "" if len(sys.argv) < 2 else sys.argv[1]

    # Make the POST request with the letter as a parameter
    payload = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        # Try to parse the JSON response
        data = response.json()

        # Check if the JSON is not empty and properly formatted
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")

    except ValueError:
        # Handle the case when the JSON is not properly formatted
        print("Not a valid JSON")

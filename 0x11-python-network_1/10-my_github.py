#!/usr/bin/python3
"""
Python script that takes GitHub credentials(username and personal access token)
and uses the GitHub API to display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) < 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    # Set up the API endpoint
    url = 'https://api.github.com/user'

    # Set up the authentication with the personal access token
    auth = (username, token)

    # Make the request to the GitHub API
    response = requests.get(url, auth=auth)

    try:
        # Try to parse the JSON response
        data = response.json()

        # Check if the JSON is not empty and properly formatted
        if data.get('id') is not None:
            print(data['id'])
        else:
            print("None")

    except ValueError:
        # Handle the case when the JSON is not properly formatted
        print("None")

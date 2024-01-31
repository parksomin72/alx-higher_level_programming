#!/usr/bin/python3
"""
List 10 commits (from the most recent to oldest) of a GitHub repository by a user.
"""
import requests
from sys import argv

if __name__ == '__main__':
    repository_name = argv[1]
    owner_name = argv[2]

    # GitHub API endpoint for listing commits
    api_url = f'https://api.github.com/repos/{owner_name}/' \
           f'{repository_name}/commits'

    # Make a GET request to the GitHub API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        commits = response.json()[:10]  # Get the 10 most recent commits

        # Print each commit in the specified format
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch commits."
      f" Status code: {response.status_code}")

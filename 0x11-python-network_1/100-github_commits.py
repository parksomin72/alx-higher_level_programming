#!/usr/bin/python3
"""
Query GitHub API for user's commits in a repository.
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    repository = argv[1]
    owner = argv[2]

    url = f'https://api.github.com/repos/{owner}/{repository}/commits'
    commits = requests.get(url, auth=HTTPBasicAuth(owner, argv[3])).json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")

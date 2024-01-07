#!/usr/bin/python3
import requests
import sys

if len(sys.argv) != 3:
    sys.exit(1)

repo_name = sys.argv[1]
owner_name = sys.argv[2]
url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'

try:
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f'{sha}: {author_name}')

except ValueError:
    print("Error fetching data from GitHub API")

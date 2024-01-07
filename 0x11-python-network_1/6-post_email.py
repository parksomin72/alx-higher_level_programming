#!/usr/bin/python3
import requests
import sys

if len(sys.argv) < 3:
    sys.exit(1)

url = sys.argv[1].rstrip()
email = sys.argv[2]

endpoint = '/post_email'
full_url = f"{url.rstrip('/')}{endpoint}"

data = {'email': email}
response = requests.post(full_url, data=data)

print("Your email is:", response.text)
print("Full URL:", full_url)

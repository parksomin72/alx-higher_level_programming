#!/usr/bin/python3
import urllib.request
import sys
if len(sys.argv) < 2:
sys.exit(1)
url = sys.argv[1]
with urllib.request.urlopen(url) as response:
x_request_id = response.headers.get('X-Request-Id')
print(x_request_id)

#!/bin/bash
# Sends a request to a URL and displays only the status code of the response

URL=$1

# Use curl to send a HEAD request and display only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$URL"

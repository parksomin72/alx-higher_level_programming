#!/bin/bash
# Script to send a GET request to a URL and display the body (for 200 status code only)
curl -sL -w "%{http_code}" "$1" -o /dev/null --write-out '\n' | grep "200" && curl -s "$1"


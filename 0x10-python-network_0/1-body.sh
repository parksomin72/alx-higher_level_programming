#!/bin/bash
set -x
# Script to send a GET request to a URL and display the body (for 200 status code only)
curl -s -o /dev/null -w "%{http_code}" "$1" | grep "200" && curl -s "$1"

#!/bin/bash

# Check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send GET request and display body only for 200 status code
response=$(curl -s -w "%{http_code}" "$1")

status_code=${response: -3}  # Extract last 3 characters (status code)
body=${response%???}         # Remove last 3 characters (status code)

if [ "$status_code" -eq 200 ]; then
  echo "$body"
fi

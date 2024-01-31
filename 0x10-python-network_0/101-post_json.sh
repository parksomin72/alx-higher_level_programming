#!/bin/bash

url=$1
json_file=$2

# Function to check if the JSON is valid
is_valid_json() {
  if python3 -m json.tool "$1" > /dev/null 2>&1; then
    echo "Valid JSON"
    return 0
  else
    echo "Not a valid JSON"
    return 1
  fi
}

# Check if the JSON is valid
if is_valid_json "$json_file"; then
  # Send POST request
  response=$(
    curl -sX POST \
      -H "Content-Type: application/json" \
      --data @"$json_file" \
      "$url"
  )
  echo "$response"
else
  echo "Not a valid JSON"
fi

#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response

URL=$1
JSON_FILE=$2

# Use curl to send a POST request with the contents of the JSON file in the body
response=$(curl -sX POST "$URL" -H "Content-Type: application/json" -d @"$JSON_FILE")

# Check if the response contains "Valid JSON" to determine the output
if [[ $response == *"Valid JSON"* ]]; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
fi

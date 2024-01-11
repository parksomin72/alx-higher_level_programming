#!/bin/bash

# Send a GET request to the URL and display the body of the response
curl -sL -w "%{http_code}" "$1" -o /dev/null | {
    read -r status
    if [ "$status" -eq 200 ]; then
        curl -sL "$1"
    fi
}

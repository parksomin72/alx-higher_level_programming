#!/bin/bash
# Script to retrieve the body size of a URL using curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

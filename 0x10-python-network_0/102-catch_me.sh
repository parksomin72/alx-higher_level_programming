#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me

# Make the request with curl, follow redirects, and set the user-agent header
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" http://0.0.0.0:5000/catch_me

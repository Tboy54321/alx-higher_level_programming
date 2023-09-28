#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL=$1

RESPONSE=$(curl -sI $URL | grep -i content-length | awk '{print $2}' | tr -d '\r')

if [ -z "$RESPONSE" ]; then
	echo "Error: Unable to retrieve response size."
else
	echo "$RESPONSE"
fi

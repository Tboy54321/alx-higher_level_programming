#!/bin/bash

# Check if a URL is provided as an argument

RESPONSE=$(curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r')

echo "$RESPONSE"


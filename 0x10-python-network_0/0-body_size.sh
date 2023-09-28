#!/bin/bash
# Check if a URL is provided as an argument
curl -sI "$1" | awk '/Content-Length/{print $2}'

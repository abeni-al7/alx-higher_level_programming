#!/usr/bin/env bash
# This script displays the size of the body of the response
# it gets from the URL it sends the request to
# The URL is provided as an argument
curl -sI $1 | grep -i Content-Length | awk {'print $2'}
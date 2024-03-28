#!/bin/bash
# This script displays the body of response of a URL
curl -sL -w "%{http_code}" -o /dev/null "$1" | grep -q "200" && curl -sL "$1"

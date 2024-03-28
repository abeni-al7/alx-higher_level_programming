#!/bin/bash
# This script sends a POST request to the passed URL
curl -X POST -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

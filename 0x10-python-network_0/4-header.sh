#!/bin/bash
# This script sends a header variable to a URL
curl -H "X-School-User-Id: 98" -s "$1"

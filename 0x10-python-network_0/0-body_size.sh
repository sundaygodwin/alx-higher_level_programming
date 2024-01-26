#!/bin/bash
# Sends a request to URL, and displays the size of its response body
curl -s "${1}" | wc -c

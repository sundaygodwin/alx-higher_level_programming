#!/bin/bash
# Sends a DELETE request to URL passed as the first argument and displays the body of response
curl -s -X DELETE "${1}"

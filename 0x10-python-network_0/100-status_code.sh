#!/bin/bash
# Sends a request to a URL passed as argument, and displays only the status code of response
curl -so /dev/null -w "%{http_code}" "$1"

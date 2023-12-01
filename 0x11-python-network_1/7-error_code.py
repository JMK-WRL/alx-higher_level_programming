#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the body. If the HTTP status code is greater than or equal to 400,
prints an error message.
"""

import requests
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
else:
    print("Usage: ./7-error_code.py <URL>")

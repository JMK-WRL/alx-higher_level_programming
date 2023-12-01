#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the body. Handles urllib.error.HTTPError exceptions.
"""

from urllib import request, error
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except error.HTTPError as e:
        print("Error code:", e.code)
else:
    print("Usage: ./3-error_code.py <URL>")

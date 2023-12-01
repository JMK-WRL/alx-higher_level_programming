#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header.
"""

from urllib import request
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]
    with request.urlopen(url) as response:
        x_request_id = response.info().get('X-Request-Id')
        print(x_request_id)
else:
    print("Usage: ./1-hbtn_header.py <URL>")

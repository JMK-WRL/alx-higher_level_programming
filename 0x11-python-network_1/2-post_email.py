#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body.
"""

from urllib import request, parse
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
else:
    print("Usage: ./2-post_email.py <URL> <email>")

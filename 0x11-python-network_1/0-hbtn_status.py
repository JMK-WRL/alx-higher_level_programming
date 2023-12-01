#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib import request

url = "https://alx-intranet.hbtn.io/status"

with request.urlopen(url) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print("\t- type:", type(body))
print("\t- content:", body)
print("\t- utf8 content:", utf8_content)

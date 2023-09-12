#!/usr/bin/python3
"""
Adds all the arguments to a python list + saves to file.
"""
import sys
import json


try:
    with open('add_item.json', 'r') as f:
        cont_r = f.read()
        cont = json.loads(cont_r)
        for arg in sys.argv[1:]:
            cont.append(arg)
        cont_r = json.dumps(cont)
    with open('add_item.json', 'w') as f:
        f.write(cont_r)
except Exception:
    with open('add_item.json', 'w') as f:
        cont = []
        for arg in sys.argv[1:]:
            cont.append(arg)
        cont_r = json.dumps(cont)
        f.write(cont_r)
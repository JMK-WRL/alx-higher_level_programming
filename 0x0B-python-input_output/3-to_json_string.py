#!/usr/bin/python3
"""Returns a JSON representation of a string"""
import json


def to_json_string(my_obj):
    """
    Function returns JSON representation
    """
    return json.dumps(my_obj)
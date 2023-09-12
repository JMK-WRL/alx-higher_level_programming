#!/usr/bin/python3
"""class define lookup """


def lookup(obj):
    """
    This function takes an objext as input and returns a list of its attributes

    Args:
        obj(object): the object to inspect
    """
    return dir(obj)

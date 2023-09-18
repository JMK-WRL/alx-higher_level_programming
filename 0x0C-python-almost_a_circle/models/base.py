#!/usr/bin/python3
"""Class base"""
import json

class Base:
    """Base class to manage IDs for other classes in the project."""

    __nb_objects = 0  

    def __init__(self, id=None):
        """
        Constructor for the Base class.

        Args:
            id (int, optional): An integer ID for the instance. If provided, it will be assigned as the ID.
                If not provided, a new ID will be generated automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string rep.

        Args:
            list_dictionaries (list): a list of dictionaries to be converted
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
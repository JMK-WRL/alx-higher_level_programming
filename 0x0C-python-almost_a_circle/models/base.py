#!/usr/bin/python3
"""Class base"""

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

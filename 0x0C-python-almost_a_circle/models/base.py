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
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted to JSON.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances to be saved to a JSON file.
        """
        filename = cls.__name__ + ".json"
        data = []

        if list_objs is not None:
            data = [obj.to_dictionary() for obj in list_objs]

        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(cls.to_json_string(data))
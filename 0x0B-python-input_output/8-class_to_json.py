def class_to_json(obj):
    """
    Return a dictionary description of an object with serializable attributes.

    :param obj: The object to be serialized.
    :return: A dictionary representation of the object's attributes.
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            json_dict[key] = value
    return json_dict

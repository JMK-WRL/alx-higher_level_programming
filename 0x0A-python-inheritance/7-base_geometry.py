#!/usr/bin/python3
"""Module of class BaseGeometry"""


class BaseGeometry:
    """Class of Base Geometry"""
    def area(self):
        """
        Raise an Exception with the message "area() is not implemented."

        Raises:
            Exception: Always raises an exception with the specified message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the integer value.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

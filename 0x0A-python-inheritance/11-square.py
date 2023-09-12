#!/usr/bin/python3
"""class square"""


class Square(Rectangle):
    """ classs that defines a sqaure rectangle"""
    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

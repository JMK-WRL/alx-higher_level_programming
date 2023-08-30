#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """Represents a square: private instance att

    Att:
        __size (int): private instance att
        __position (tuple): private instance att
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new instance of the square class.

        Args:
            size: the size of the square
            position: position of the square (tuple)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size att

        Returns:
            int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size att

        Args:
            value: the new size to set (int)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position att

        Returns:
            tuple: position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute

        Args:
            value: new position to set (tuple).

        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive inetegrs")
        self.__position = value

    def area(self):
        """
        Computes and resturns the are of the square.

        returns:
            int: area of the sqaure.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#' characters
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string rep of the square
        """
        result = []
        for _ in range(self.__position[1]):
            result.append("")
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)

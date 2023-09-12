#!/usr/bin/python3
"""Method rectangle"""


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """
        Initialize a rectangle instance

        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle

        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        def area(self):
            """Calculates the area of the rectangle

                Returns: 
                    int: the area of the rectangle
            """

            return self.__width * self.__height
        
        def __str__(self):
            """
            Return a string representation of the rectangle
            """

            return "[Rectangle] {}/{}".format(self.__width, self.__height)
#!/usr/bin/python3
#4-print_square


def print_square(size):
    """Prints a square with the charcter '#' 
    
    Args:
        size(int): length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for _ in range(size):
        print("#" * size)
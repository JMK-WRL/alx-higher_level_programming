#!/usr/bin/python3
# 2-matrix_dividend.py
""" Defines a matrix division function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix divisor.

    Args:
        matrix: matrix to be divided
        div (int or float): the divisor

    """
    if not all(isinstance(row, list) and all (isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
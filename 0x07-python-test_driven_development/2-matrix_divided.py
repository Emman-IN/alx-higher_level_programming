#!/usr/bin/python3
"""The matrix division module"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix
    Args:
        matrix (list): list of lists
        div (int, float): divides numbers in matrix
    """
    if (type(matrix) is not list or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, int) or isinstance(ele, float)
                for ele in [num for rows in matrix for num in rows])):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for i in range(len(matrix)):
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(num/div, 2) for num in row] for row in matrix]

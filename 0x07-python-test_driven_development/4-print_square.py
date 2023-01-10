#!/usr/bin/python3
"""the print square module"""


def print_square(size):
    """prints a square with the character #
    Args:
        size (int): the size of the square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        print('{}'.format('#'*size))

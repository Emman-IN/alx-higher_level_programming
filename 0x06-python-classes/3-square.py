#!/usr/bin/python3
"""implemenntation of the Square class"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """initialize the square with attributes
        Args:
            size (int): The square's size
            """
        if type(size) is  not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size**2

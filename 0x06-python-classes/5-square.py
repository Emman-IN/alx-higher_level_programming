#!/usr/bin/python3
"""implemenntation of the Square class"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """initialize the square with attributes
        Args:
            size (int): The square's size
        """
        self.__size = size

    @property
    def size(self):
        """getter function to return the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the size private attribute
        Args:
            value (int): the value of the square
         """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size**2

    def my_print(self):
        for i in range(self.__size):
            print('{}'.format('#'*self.__size))

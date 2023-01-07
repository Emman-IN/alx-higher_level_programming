#!/usr/bin/python3
"""Implementation of the Square class"""


class Square():
    """The Square class itself"""

    def __init__(self, size=0, position=(0, 0)):
        """initializes instance attributes
        Args:
            size: size of the square
            position: cordinates of the square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """gets the value of the sie of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of the size of the square
        Args:
            value: size of the square to be set"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the square's area"""
        return self.__size**2

    @property
    def position(self):
        """returns the square's co-ordinate"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the co-ordinates of the square
        Args:
            value: cordinates of the square"""
        if (type(value) is not tuple and len(value) != 2
                and not all(isinstance(num, int) for num in value)
                and not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print('{}{}'.format(' '*self.__position[0], '#'*self.__size))

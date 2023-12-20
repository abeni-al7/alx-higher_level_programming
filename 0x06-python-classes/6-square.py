#!/usr/bin/python3
"""
Defines a class with attributes.
"""


class Square:
    """
    A simple square class with attributes.

    Attributes:
        size (int): the length of the side of the square
        position (tuple): space position

    Methods:
        area(): area of the square
        my_print(): prints the square object
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2 or not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            lines, spaces = self.__position
            for i in range(lines):
                print()
            for i in range(self.__size):
                for j in range(spaces):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

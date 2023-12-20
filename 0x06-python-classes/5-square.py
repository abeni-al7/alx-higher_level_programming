#!/usr/bin/python3
"""
Defines a class with attributes.
"""


class Square:
    """
     A simple square class with attributes.
     
     Attributes:
        size (int): the length of the side of the square
 
    Methods:
        area: area of the square
        my_print: prints the square object
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        return self.__size * self.__size
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

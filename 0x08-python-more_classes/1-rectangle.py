#!/usr/bin/python3
"""
A module that defines a rectangle class
"""


class Rectangle:
    """
    A Rectangle class with attributes.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        if isinstance(self.__width) != int:
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')

    @property
    def width(self):
        return self.__width

    @width.setter
    def  width(self, value):
        if isinstance(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if isinstance(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
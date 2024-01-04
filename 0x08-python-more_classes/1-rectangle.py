#!/usr/bin/python3
"""
A module that defines a rectangle class
"""


class Rectangle:
    """
    A Rectangle class with attributes.
    """

    def __init__(self, width=0, height=0):
        """Initializer for object.

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def  width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

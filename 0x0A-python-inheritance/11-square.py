#!/usr/bin/python3
"""A Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class"""

    def __init__(self, size):
        """Initialize the rectangle class."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate area of rectangle"""
        return self.__size * self.__size

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__size, self.__size)

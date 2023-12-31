#!/usr/bin/python3
"""A Rectangle class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class"""

    def __init__(self, width, height):
        """Initialize the rectangle class."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(type(self).__name__, 
            self.__width, self.__height)

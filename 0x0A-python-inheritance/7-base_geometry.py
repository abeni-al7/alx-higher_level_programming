#!/usr/bin/python3
"""A class with methods
"""


class BaseGeometry:
    """A class with methods"""

    def area(self):
        """Unimplemented area method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """An integer validator function"""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

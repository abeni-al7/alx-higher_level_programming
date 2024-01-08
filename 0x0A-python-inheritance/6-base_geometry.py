#!/usr/bin/python3
"""A class with a problematic method
"""


class BaseGeometry:
    """A class with a method that raises exception"""

    def area(self):
        """Unimplemented area method"""
        raise Exception('area() is not implemented')

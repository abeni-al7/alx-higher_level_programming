#!/usr/bin/python3
""" A module containing a student class
"""

class Student:
    """ A student class
    """


    def __init__(self, first_name, last_name, age):
        """A method that initializes a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student"""
        my_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
        return my_dict

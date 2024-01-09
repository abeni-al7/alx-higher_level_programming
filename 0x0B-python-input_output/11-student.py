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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student"""
        my_dict = {}
        if isinstance(attrs, list):
            if "first_name" in attrs:
                my_dict["first_name"] = self.first_name
            if "last_name" in attrs:
                my_dict["last_name"] = self.last_name
            if "age" in attrs:
                my_dict["age"] = self.age
        else:
            my_dict["first_name"] = self.first_name
            my_dict["last_name"] = self.last_name
            my_dict["age"] = self.age
        return my_dict

    def reload_from_json(self, json):
        """Replaces all attributes of Student"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)

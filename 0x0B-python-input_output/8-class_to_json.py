#!/usr/bin/python3
"""A module for returning all attributes of an object"""


def class_to_json(obj):
    """A function that returns all attributes of an object"""
    my_dict = obj.__dict__
    return my_dict

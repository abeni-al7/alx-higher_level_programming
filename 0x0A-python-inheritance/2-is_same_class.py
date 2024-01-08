#!/usr/bin/python3
"""Module to check for the same object
"""


def is_same_class(obj, a_class):
    """Function to check for the same object"""
    if not type(obj) == a_class:
        return False
    else:
        return True

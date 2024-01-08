#!/usr/bin/python3
"""Module to check for subclass
"""


def inherits_from(obj, a_class):
    """Function to check for subclass"""
    if issubclass(obj, a_class):
        return True
    return False

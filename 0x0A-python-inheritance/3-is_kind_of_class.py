#!/usr/bin/python3
"""Module to check for same or inheritance class cases
"""


def is_kind_of_class(obj, a_class):
    """Function to check for same or inheritance class cases"""
    if isinstance(obj, a_class):
        return True
    return False

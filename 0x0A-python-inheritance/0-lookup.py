#!/usr/bin/python3
"""Module to return the list of available attributes of an object
"""


def lookup(obj):
    """Function to return list of available attributes and methods"""
    keys = dir(obj)
    return keys

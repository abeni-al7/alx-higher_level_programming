#!/usr/bin/python3
"""
A module that prints the name of a person
"""


def say_my_name(first_name, last_name=""):
    """A function that prints the name of a person."""

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))

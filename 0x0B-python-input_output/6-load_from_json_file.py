#!/usr/bin/python3
"""A module for deserializing an object from a file"""
import json


def load_from_json_file(filename):
    """A function that deserializes from a file"""
    my_obj = None
    data = None
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    my_obj = data
    return my_obj

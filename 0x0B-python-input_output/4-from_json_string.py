#!/usr/bin/python3
"""A module for deserializing an object"""
import json


def from_json_string(my_str):
    """A function that deserializes an object"""
    return json.loads(my_str)

#!/usr/bin/python3
"""A module for serializing an object"""
import json


def to_json_string(my_obj):
    """A function that serializes an object"""
    return json.dumps(my_obj) 

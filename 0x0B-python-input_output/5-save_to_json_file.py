#!/usr/bin/python3
"""A module for serializing an object and storing it in a file"""
import json


def save_to_json_file(my_obj, filename):
    """A function that serializes an object and stores it in a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f) 

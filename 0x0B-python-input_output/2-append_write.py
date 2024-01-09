#!/usr/bin/python3
"""A module for appending to a file"""


def append_write(filename="", text=""):
    """A function that appends to a file"""
    count = 0
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
    return count

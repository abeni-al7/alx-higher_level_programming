#!/usr/bin/python3
"""A module for writing to a file"""


def write_file(filename="", text=""):
    """A function that writes to a file"""
    count = 0
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
    return count

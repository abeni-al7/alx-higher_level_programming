#!/usr/bin/python3
"""A module for reading a file"""


def read_file(filename=""):
    """A function that reads a file"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")

#!/usr/bin/python3
"""Module to create a child class of 'list'
"""


class MyList(list):
    """A subclass of the list class"""

    def __init__(self, *args):
        super().__init__(*args)

    def print_sorted(self):
        """Function to print a sorted list"""
        new_list = self[:]
        new_list.sort()
        print(new_list)

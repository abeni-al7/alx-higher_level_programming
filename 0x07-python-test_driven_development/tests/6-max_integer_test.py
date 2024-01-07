#!/usr/bin/python3
"""Unittest for max_integer which returns the max int in a list.
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """A class that contains the test functions"""


    def test_max(self):
        """Test functionality of function"""
        my_list = [1, 2, 3, 4]
        result = max_integer(my_list)
        self.assertEqual(result, 4)
    def test_noelements(self):
        """Test edge case where no elements exist"""
        my_list = []
        result = max_integer(my_list)
        self.assertEqual(result, None)

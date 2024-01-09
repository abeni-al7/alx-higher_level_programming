#!/usr/bin/python3
""" A module containing a student class
"""


def pascal_triangle(n):
    """A function that creates a pascal triangle"""
    if n <= 0:
        return []
    my_list = []
    for i in range(n):
        nums = []
        for j in range(i + 1):
            if j == 0 or j == i:
                nums.append(1)
            else:
                if j < len(my_list[i - 1]):
                    nums.append(my_list[i - 1][j - 1] + my_list[i - 1][j])
        my_list.append(nums)
    return my_list

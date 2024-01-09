#!/usr/bin/python3
"""A module for adding cl args to a list and saves it"""
import json
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    my_list = load("add_item.json")
except Exception:
    my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save(my_list, "add_item.json")

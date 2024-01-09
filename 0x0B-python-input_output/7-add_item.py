#!/usr/bin/python3
"""A module for adding cl args to a list and saves it"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if isinstance(load_from_json_file, list):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, "add_item.json")
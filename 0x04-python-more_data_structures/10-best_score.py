#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max = 0
    value = None
    for key in a_dictionary:
        if a_dictionary[key] > max:
            max = a_dictionary[key]
            value = key
    return value

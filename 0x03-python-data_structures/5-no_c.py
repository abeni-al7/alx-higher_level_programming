#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for character in my_string:
        if character == 'c' or character == 'C':
            continue
        new_str += character
    return new_str

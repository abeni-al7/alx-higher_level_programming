#!/usr/bin/python3
"""
A module that indents text
"""


def text_indentation(text):
    """A function that indents text."""

    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        elif i != 0 and text[i] == ' ':
            if text[i - 1] == '.' or text[i - 1] == '?' or text[i - 1] == ':':
                continue
            else:
                print(text[i], end="")
        else:
            print(text[i], end="")

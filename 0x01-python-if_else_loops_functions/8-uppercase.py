#!/usr/bin/python3
def uppercase(str):
    result = ""
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            code = ord(letter) - 32
            letter = chr(code)
        result += letter
    print(result)

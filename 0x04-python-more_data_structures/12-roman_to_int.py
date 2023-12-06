#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None:
        return None
    number = 0
    roman_dictionary = {"I": 1, "V": 5, "X": 10, 
                        "L": 50, "C": 100, "D": 500, 
                        "M": 1000}
    for i in range(len(roman_string)):
        if roman_string[i] in roman_dictionary:
            if roman_string[i] == 'V' or roman_string[i] == 'X':
                if i - 1 not in range(len(roman_string)):
                    None
                elif roman_string[i - 1] == 'I':
                    number -= 2
            if roman_string[i] == 'L' or roman_string[i] == 'C':
                if i - 1 not in range(len(roman_string)):
                    None
                elif roman_string[i - 1] == 'X':
                    number -= 20
            if roman_string[i] == 'D' or roman_string[i] == 'M':
                if i - 1 not in range(len(roman_string)):
                    None
                elif roman_string[i - 1] == 'C':
                    number -= 200
            number += roman_dictionary[roman_string[i]]

    return number

#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return None
    if not isinstance(roman_string, str):
        return None
    number = 0
    roman_dictionary = {"I": 1, "V": 5, "X": 10,
                        "L": 50, "C": 100, "D": 500,
                        "M": 1000}
    for i in range(len(roman_string)):
        if roman_string[i] in roman_dictionary:
            if i > 0 and roman_string[i - 1] in roman_dictionary:
                if roman_dictionary[roman_string[i - 1]] < roman_dictionary[roman_string[i]]:
                    number += roman_dictionary[roman_string[i]] - 2 * roman_dictionary[roman_string[i - 1]]
                else:
                    number += roman_dictionary[roman_string[i]]
            else:
                number += roman_dictionary[roman_string[i]]

    return number

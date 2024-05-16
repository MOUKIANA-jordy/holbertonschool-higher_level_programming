#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    if not roman_string or not isinstance(roman_string, str):
        return result

    _romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    for i in range(len(roman_string)):
        letter = roman_string[i]
        previous_letter = None
        if i > 0:
            try:
                previous_letter = roman_string[i - 1]
            except Exception:
                previous_letter = None

        r = _romans.get(letter, 0)
        less = None
        if previous_letter is not None:
            less = _romans[previous_letter]
        if less is not None and less < r:
            result -= (less * 2)
        result += r
    return result

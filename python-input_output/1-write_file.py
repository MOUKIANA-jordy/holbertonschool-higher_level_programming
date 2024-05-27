#!/usr/bin/python3
"""
function that writes a string to a text file
"""


def write_file(filejordy="", text=""):
    """
    Writes a string to a text file (UTF8) and
        returns the number of characters written.
    """
    with open(filejordy, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)
    return num_chars

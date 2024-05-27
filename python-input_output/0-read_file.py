#!/usr/bin/python3
"""
    function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
        Reads a text file (UTF8) and prints it to stdout.
        Arguments:
            filename (str): File to open.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

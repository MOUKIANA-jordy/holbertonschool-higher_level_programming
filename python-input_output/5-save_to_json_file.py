#!/usr/bin/python3
"""
This module provides a function to save an object to a JSON file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a file in JSON format.

    Args:
        my_obj (any): The object to save.
        filename (str): The file name.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

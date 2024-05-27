#!/usr/bin/python3
"""
function that returns the dictionary description
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple
     data structure for JSON serialization of an object.
    """
    attributes = obj.__dict__
    json_attributes = {}
    for key, value in attributes.items():
        if hasattr(value, '__dict__'):
            json_attributes[key] = class_to_json(value)
        else:
            json_attributes[key] = value

    return json_attributes

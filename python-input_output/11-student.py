#!/usr/bin/python3
"""
    File class for Student.
"""


class Student:
    """ Class of a student. """

    def __init__(self, first_name, last_name, age):
        """
            Initialization of a student.
            Arguments:
                first_name (str): First name of the student.
                last_name (str): Last name of the student.
                age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Get the json format of the Student class.
            Arguments:
                attrs (list[str], optional): List to filter.
        """
        _dict = {}
        _original_dict = self.__dict__
        if attrs is None:
            _dict = _original_dict
        else:
            for attr in attrs:
                value = _original_dict.get(attr, None)
                if value:
                    _dict[attr] = value
        return _dict

    def reload_from_json(self, json):
        """
            Replaces all attributes of the Student instance.
            Arguments:
                json (dict): To replace.
        """
        for key in json:
            val = json[key]
            setattr(self, key, val)

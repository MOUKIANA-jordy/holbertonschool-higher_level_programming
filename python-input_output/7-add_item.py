#!/usr/bin/python3
"""
script that adds all arguments to a Python list
"""


import sys
from 5-save_to_json_file __import__ save_to_json_file
from 6-load_from_json_file __import__ load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)

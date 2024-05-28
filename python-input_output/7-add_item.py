#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file.
"""

import sys
import os
from importlib import import_module

save_to_json_file = import_module('5-save_to_json_file').save_to_json_file
load_from_json_file = import_module(
                        '6-load_from_json_filei').load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])

save_to_json_file(items, filename)

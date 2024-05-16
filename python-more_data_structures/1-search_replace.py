#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for el in my_list:
        if el == search:
            el = replace
        new_list.append(el)
    return new_list

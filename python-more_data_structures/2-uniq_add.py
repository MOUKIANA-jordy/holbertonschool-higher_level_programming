#!/usr/bin/python3
def common_elements(set_1, set_2):
    cache = []
    c_set = []
    for _set in [set_1, set_2]:
        for el in _set:
            if el in cache:
                c_set.append(el)
            else:
                cache.append(el)
    return c_set

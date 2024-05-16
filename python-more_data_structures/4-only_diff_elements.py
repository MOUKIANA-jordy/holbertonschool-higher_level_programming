#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    rm_c = set_1.symmetric_difference(set_2)
    return rm_c

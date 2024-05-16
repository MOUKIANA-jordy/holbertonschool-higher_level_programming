#!/usr/bin/python3
def best_score(a_dictionary):
    _score = None
    _key_score = None
    if a_dictionary:
        for key in a_dictionary:
            if _score is None or a_dictionary[key] > _score:
                _score = a_dictionary[key]
                _key_score = key
    return _key_score

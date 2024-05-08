#!/usr/bin/python3
def islower(c):
    unicode = ord(c)
    if unicode >= 97 and unicode <= 122:
        return True
    return False

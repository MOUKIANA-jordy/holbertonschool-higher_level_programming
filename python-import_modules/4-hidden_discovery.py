#!/usr/bin/python3
from hidden_4 import *

if __name__ == "__main__":
    for s in dir():
        if s[:2] != "__":
            print(s)

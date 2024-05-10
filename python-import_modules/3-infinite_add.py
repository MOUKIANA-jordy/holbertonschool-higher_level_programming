#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    count = 0
    if argc > 0:
        for i in range(1, len(argv)):
            count += int(argv[i])
    print(count)

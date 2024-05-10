#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    print("{:d} {}{}".format(
        argc,
        "argument" if argc == 1 else "arguments",
        "." if argc < 1 else ":"
    ))
    if argc >= 1:
        for i in range(1, len(argv)):
            arg = argv[i]
            print("{}: {}".format(i, arg))

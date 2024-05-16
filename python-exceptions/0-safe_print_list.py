#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            printed_count += 1
        except Exception:
            pass
    print()

    return printed_count

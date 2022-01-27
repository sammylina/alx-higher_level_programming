#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                continue
        print()
    except IndexError:
        raise
    return count

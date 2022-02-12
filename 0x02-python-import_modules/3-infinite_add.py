#!/usr/bin/python3
"""3-infinite_add module take infinite number of integers
and print back their sum"""


if __name__ == '__main__':

    import sys

    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    print(total)

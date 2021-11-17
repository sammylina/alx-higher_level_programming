#!/usr/bin/python3
def uppercase(str):
    for i, c in enumerate(str):
        if ord(c) > 96 and ord(c) < 123:
            str = str[:i] + chr(ord(c) - 32) + str[i + 1:]
    print("{:s}".format(str), end="")
    print()

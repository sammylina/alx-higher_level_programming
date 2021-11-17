#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if islower(c):
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{:s}".format(c), end="")
    print()


def islower(c):
    if ord(c) < 123 and ord(c) > 91:
        return True
    else:
        return False

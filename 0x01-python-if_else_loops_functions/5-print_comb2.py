#!/usr/bin/python3
for c in range(100):
    if c == 99:
        print("{:d}".format(c))
    else:
        print("{:02d}".format(c), end=", ")

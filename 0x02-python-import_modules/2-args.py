#!/usr/bin/python3
"""2-args module prints back arguments passed in
to the program"""
 

if __name__ == '__main__':

    import sys

    if len(sys.argv) > 2:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for idx in range(1, len(sys.argv)):
            print('{:d}: {:s}'.format(idx, sys.argv[idx]))
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {:s}".format(sys.argv[1]))
    else:
        print("0 arguments.")

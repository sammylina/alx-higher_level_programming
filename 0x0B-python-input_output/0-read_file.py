#!/usr/bin/python3
"""read file module"""
import sys


def read_file(filename=""):
    """read a file and print to stdout

    Args:
        filename (str): string file name

    """
    with open(filename, encoding='utf-8') as a_file:
        sys.stdout.write(a_file.read())

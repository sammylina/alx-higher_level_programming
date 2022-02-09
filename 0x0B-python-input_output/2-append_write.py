#!/usr/bin/python3
"""append to a file"""


def append_write(filename="", text=""):
    """append text to file and if filename dosen't exist create it

    Args:
        filename (str): name of file
        text (str): string to append to file

    """
    with open(filename, mode='a', encoding='utf-8') as file:
        a_size = file.write(text)

    return a_size

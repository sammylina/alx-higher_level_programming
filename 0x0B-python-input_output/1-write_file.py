#!/usr/bin/python3
"""write to file module"""


def write_file(filename="", text=""):
    """overwrite filename with text and create if file dosen't exist

    Args:
        filename (str): name of the file
        text (str): string to write to the file

    """
    with open(filename, mode='w', encoding='utf-8') as file:

        size = file.write(text)
    return size

#!/usr/bin/python3
"""text_indentation module

"""


def text_indentation(text):
    """Indent a text using ', ? and : characters and
    add two newlines following the characters

    Args:
        text (str): a string text to be indented

    Raises:
        TypeError: if txt is not a string

    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    n_text = text.replace('. ', '.\n\n').replace('? ', '?\n\n').\
        replace(': ', ':\n\n')
    print(n_text, end="")

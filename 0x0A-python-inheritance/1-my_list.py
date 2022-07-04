#!/usr/bin/python3
"""Custom MyList module
"""


class MyList(list):
    """custom list object that extend the built-in
    python list object

    """

    def print_sorted(self):
        """print all items of the list in sorted order
        """
        copy = [*self]
        copy.sort()
        print(copy)

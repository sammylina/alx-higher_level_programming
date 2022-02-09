#!/usr/bin/python3
"""MyList module. extended version of python list
"""


class MyList(list):
    """Extended version of python list with
    ablity to print a sorted list in ascendin order

    Note:
        we don't need __init__ because the class is
        inherited from list class

    """
    def __init__(self, *arg):
        super().__init__([m for m in arg])

    def print_sorted(self):
        """print the list in ascending order

            Attributes:
                copy (list): copy of the original list
        """
        copy = [item for item in self]
        copy.sort()
        print(copy)

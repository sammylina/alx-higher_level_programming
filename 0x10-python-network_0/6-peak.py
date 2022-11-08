#!/usr/bin/python3
"""Find peak value
"""


def find_peak(int_list):
    """Find the peak value in the list
    """
    if len(int_list) == 0:
        return None
    else:
        peak = int_list[0]
        for elem in int_list[1:]:
            if elem > peak:
                peak = elem
        return peak

#!/usr/bin/python3
"""Find peak module
"""


def find_peak(int_list):
    """Find any peak value in the list
    """
    print("list: ", int_list)
    if len(int_list) == 0:
        return None
    if len(int_list) == 1:
        return int_list[0]
    else:
        s = (len(int_list) // 2)
        print("split at: ", s)
        if int_list[s] >= int_list[s-1] and int_list[s] >= int_list[s+1]:
            return int_list[s]
        else:
            if int_list[s] <= int_list[s+1]:
                return find_peak(int_list[s:])
            else:
                return find_peak(int_list[:s+1])

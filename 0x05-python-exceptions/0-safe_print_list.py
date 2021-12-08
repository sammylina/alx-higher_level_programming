#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    while True and index < x:
        try:
            print(my_list[index], end="")
            i++
        except IndexError:
            break
    print()
    return index

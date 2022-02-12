#!/usr/bin/python3
"""4-hidden_discover module print names in compiled file"""

if __name__ == '__main__':
    import hidden_4

    for name in dir(hidden_4):
        if name[0] != '_':
            print(name)

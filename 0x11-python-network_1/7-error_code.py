#!/usr/bin/python3
"""send post request using requests module
"""


if __name__ == '__main__':

    import requests as req
    import sys

    url = sys.argv[1]
    res = req.get(url)
    if 400 <= res.status_code:
        print("Error code:", res.status_code)
    else:
        print(res.text)

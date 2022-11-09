#!/usr/bin/python3
"""send post request using requests module
"""


if __name__ == '__main__':

    import requests as req
    import sys

    url, email = sys.argv[1:3]
    res = req.post(url, data={'email': email})
    print(res.text)

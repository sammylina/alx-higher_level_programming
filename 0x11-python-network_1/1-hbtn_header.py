#!/usr/bin/python3
"""hbtn_header module
"""


if __name__ == '__main__':

    import urllib.request as request
    import sys

    url = sys.argv[1]
    req_obj = request.Request(url)
    with request.urlopen(req_obj) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))

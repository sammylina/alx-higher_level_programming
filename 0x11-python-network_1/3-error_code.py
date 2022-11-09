#!/usr/bin/python3
"""handle HTTPError and print status code
"""


if __name__ == '__main__':

    from urllib.error import HTTPError, URLError
    import urllib.request as request
    import sys

    url = sys.argv[1]
    req_obj = request.Request(url)
    try:
        with request.urlopen(req_obj) as res:
            print(res.read().decode('utf8'))
    except HTTPError as err:
        print("Error code:", err.code)

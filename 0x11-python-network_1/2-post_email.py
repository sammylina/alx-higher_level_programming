#!/usr/bin/python3
"""post email to endpoint
"""


if __name__ == '__main__':

    import urllib.parse as parse
    import urllib.request as request
    import sys

    url, email = sys.argv[1:3]
    data = parse.urlencode({'email': email})
    data = data.encode('ascii')
    req_obj = request.Request(url, data)
    with request.urlopen(req_obj) as res:
        print(res.read().decode('utf8'))

#!/usr/bin/python3
"""hbtn_status module
"""


if __name__ == '__main__':
    import urllib.request as request

    url = 'https://alx-intranet.hbtn.io/status'
    req = request.Request(url)
    with request.urlopen(req) as res:
        data = res.read()
        print('     - type: {}'.format(type(data)))
        print('     - content: {}'.format(data))
        print('     - utf8 content: {}'.format(data.decode('utf8')))

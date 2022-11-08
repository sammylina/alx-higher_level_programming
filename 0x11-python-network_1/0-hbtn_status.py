#!/usr/bin/python3
"""hbtn_status module
"""


if __name__ == '__main__':
    import urllib.request as request

    url = 'https://alx-intranet.hbtn.io/status'
    req = request.Request(url)
    with request.urlopen(req) as res:
        data = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(data))
        print('\t- utf8 content: {}'.format(data.decode('utf8')))

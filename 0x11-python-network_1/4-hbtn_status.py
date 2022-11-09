#!/usr/bin/python3
"""check status if alx-intranet using requests module
"""


if __name__ == '__main__':

    import requests as req

    res = req.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(res.text)))
    print('\t- content: {}'.format(res.text))

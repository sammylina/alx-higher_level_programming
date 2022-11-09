#!/usr/bin/python3
"""print JSON response
"""


if __name__ == '__main__':

    import requests as req
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    q_str = sys.argv[1] if (len(sys.argv) == 2) else ""
    res = req.post(url, data={'q': q_str})
    try:
        user = res.json()
        if len(user) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(user.get('id'), user.get('name')))
    except Exception as e:
        print("Not a valid JSON")

#!/usr/bin/python3
"""fetch your id from github api
"""


if __name__ == '__main__':

    import requests as req
    import sys

    username, token = sys.argv[1:3]
    res = req.get('https://api.github.com/users/{}'.format(username),
                  headers={'Accept': 'application/vnd.github+json',
                           'Authorization': 'Bearer {}'.format(token)})
    try:
        print(res.json().get('id'))
    except Exception:
        print(None)

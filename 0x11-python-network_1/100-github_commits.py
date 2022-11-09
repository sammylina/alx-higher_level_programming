#!/usr/bin/python3
"""fetch commits from github api
"""


if __name__ == '__main__':

    import requests as req
    import sys

    repo, owner = sys.argv[1:3]
    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'
    res = req.get(url.format(owner, repo),
                  headers={'Accept': 'application/vnd.github+json'})

    for item in res.json():
        print('{}: {}'.format(item.get('sha'),
              item.get('commit').get('author').get('name')))

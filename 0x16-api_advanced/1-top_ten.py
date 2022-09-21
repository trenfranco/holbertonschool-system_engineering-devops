#!/usr/bin/python3
""""prints the titles of the first 10 hot posts listed for a given subreddit"""

import json
import requests


def top_ten(subreddit):
    """gives top 10 title name of posts"""

    headers = {'User-Agent': 'myAPI'}

    res = requests.get("https://www.reddit.com/r/{}/hot.json"
                       .format(subreddit), headers=headers,
                       allow_redirects=False)
    if res.status_code == 200:
        top10 = 0
        for k in res.json()["data"]["children"]:
            if top10 < 10:
                print(k["data"]["title"])
            top10 += 1
    else:
        print(None)

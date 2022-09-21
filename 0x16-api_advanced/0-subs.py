#!/usr/bin/python3
"""from Reddit´sAPI returns number of subscribers for a given sub"""

import json
import requests


def number_of_subscribers(subreddit):
    """returns number of followers a subReddit has using Reddit API"""

    """identify ourselves"""
    headers = {'User-Agent': 'MyAPI'}

    res = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers=headers, allow_redirects=False)
    if res.status_code == 200:
        return res.json()['data']['subscribers']
    return 0

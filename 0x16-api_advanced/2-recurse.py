#!/usr/bin/python3
"""returns list of all hot posts"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive func"""

    headers = {'User-Agent': 'MyAPI'}
    params = {'after': after}
    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            headers=headers,
                            params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        top = response.json().get('data').get('children')
        for post in top:
            hot_list.append(post.get('data').get('children'))
        after = response.json().get('data').get('after')
        if after is None:
            return (hot_list)
        else:
            return (recurse(subreddit, hot_list, after))
    else:
        return (None)

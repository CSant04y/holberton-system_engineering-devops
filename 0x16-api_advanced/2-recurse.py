#!/usr/bin/bash
"""[This is a recursive function]
"""


def recurse(subreddit, hot_list=[], after=None, count=0):
    """[Queries the Reddit API returns list
     of titles of hot posts for subreddits]
    """
    import json
    import requests

    if after is None:
        URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        URL = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)

    response = requests.get(URL, headers={"user-agent": "user"},
                            allow_redirects=False).json()

    if "data" not in response and hot_list == []:
        return None
    children = response.get('data').get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))
        count += 1
    after = response.get('data').get('title')
    if after is None:
        return hot_list
    return (recurse(subreddit, hot_list, after, count))

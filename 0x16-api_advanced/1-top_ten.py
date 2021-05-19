#!/usr/bin/python3
"""
Gets top ten hottest post from subreddit
"""

import json
import requests


def top_ten(subreddit):
    """[This gets the top ten hot posts listed from a given subreddit]

    Args:
        subreddit ([string]): [subbreddit to be searched]
    """

    URL = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    response = requests.get(URL, headers={"user-agent": "user"},
                            allow_redirects=False).json()
    if "data" not in response:
        print("None")
        return

    children = response.get("data").get("children")

    for child in children:
        print(child.get("data").get("title"))

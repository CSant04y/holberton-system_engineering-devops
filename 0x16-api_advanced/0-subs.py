#!/usr/bin/python3
"""[This queries the Reddit API]
"""

import requests
from requests.models import Response


def number_of_subscribers(subreddit):
    """[This gets the Total number of subscribers from the reddit API]

    Args:
        subreddit ([string]): [argument passes to be searched]
    """
    URL = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    Response = requests.get(URL, headers={"user-agent": "user"},
                            allow_redirects=False).json()

    if 'data' not in Response:
        return 0

    return Response.get('data').get('subscribers')

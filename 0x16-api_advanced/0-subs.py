#!/usr/bin/python3
"""
File that contains a function that queries Reddit API
https://www.reddit.com/dev/api/
and returns the number of subscribers (not active users, total subscribers)\
for a given subreddit.
if an invalid subreddit is given, the function should return 0.
"""
import requests
from typing import Union


def number_of_subscribers(subreddit: str) -> int:
    """
    Function that gets the number of subscribers for a subreddit.

    Args:
        subreddit (str): String represents subreddit.

    Returns: number of subscribers as in python integers
    """
    # Build the url
    url: str = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # User agent variable
    user_agent: str = "For good purpose"
    # Headers
    headers = {"User-Agent": user_agent}
    # Make the request
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Get the data
        data = response.json().get("data")
        # Get the number of subscribers
        subscribers: Union[int, None] = data.get("subscribers")
        if subscribers is None:
            return 0
        else:
            return subscribers
    return 0

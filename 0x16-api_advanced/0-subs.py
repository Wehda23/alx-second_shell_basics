#!/usr/bin/python3
"""
File that contains a function that queries Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that gets the number of subscribers for a subreddit.
    """
    # Build the url
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # User agent variable
    user_agent = "For good purpose"
    # Headers
    headers = {"User-Agent": user_agent}
    # Make the request
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Get the data
        data = response.json().get("data")
        # Get the number of subscribers
        subscribers = data.get("subscribers")
        if subscribers is None:
            return 0
        else:
            return subscribers
    return 0

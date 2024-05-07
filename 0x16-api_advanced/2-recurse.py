#!/usr/bin/python3
"""
File that contains a function that queries Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function that returns the titles of hot posts.
    """
    # Build the URL for the current page
    url = "https://www.reddit.com/r/{}/hot.json?limit=100{}".format(
        subreddit, after if after else ""
    )
    # User agent variable
    user_agent = "For good purpose"
    # Headers
    headers = {"User-Agent": user_agent}
    # Make the request
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Get the data
        data = response.json().get("data")
        if data:
            # Get the children (posts)
            posts = data.get("children")
            for post in posts:
                # Append the title of each post to hot_list
                hot_list.append(post.get("data").get("title"))
            # Recursively call recurse function with the next page
            next_page = data.get("after")
            if next_page:
                next_page = "&after={}".format(next_page)
                return recurse(subreddit, hot_list, next_page)
            else:
                return hot_list
        else:
            return None
    else:
        return None

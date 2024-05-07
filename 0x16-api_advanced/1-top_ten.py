#!/usr/bin/python3
"""
File that contains a function that queries Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Function that prints the titles of the first 10 hot posts.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
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
                # Print the title of each post
                print(post.get("data").get("title"))
        else:
            print(None)
    else:
        print(None)

#!/usr/bin/python3
"""
File that contains a recursive function that queries Reddit API
https://www.reddit.com/dev/api/
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces).
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursive function that queries Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): Subreddit to search.
        word_list (list): List of keywords to count occurrences.

    Returns:
        None
    """
    # Initialize counts dictionary if not provided
    if counts is None:
        counts = Counter()

    # Build the URL for the current page
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)

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
                # Get the title of the post
                title = post.get("data").get("title")
                # Convert title to lowercase for case-insensitive comparison
                title_lower = title.lower()
                # Count occurrences of keywords in the title
                for word in word_list:
                    if word.lower() in title_lower.split():
                        counts[word.lower()] += 1
            # Recursively call count_words function with the next page
            after = data.get("after")
            if after and after not in url:
                return count_words(subreddit, word_list, after, counts)
            else:
                # Print the sorted count of keywords
                for word, count in sorted(
                    counts.items(), key=lambda x: (-x[1], x[0])
                ):
                    print(f"{word}: {count}")
        else:
            # No posts found
            return
    else:
        # Invalid subreddit or other error
        return

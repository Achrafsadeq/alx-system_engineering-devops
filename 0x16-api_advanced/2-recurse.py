#!/usr/bin/python3
"""
Module to interact with the Reddit API
"""

import requests
import re
from collections import Counter


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store article titles.
        after (str): Parameter for pagination.

    Returns:
        list: A list of hot article titles,
        or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    params = {'after': after, 'limit': 100}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        for post in posts:
            hot_list.append(post.get("data", {}).get("title"))
        after = data.get("data", {}).get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None

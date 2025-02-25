#!/usr/bin/python3
"""
Module to interact with the Reddit API
"""

import requests
import re
from collections import Counter


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).
    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        counts (dict): Dictionary to store keyword counts.
        after (str): Parameter for pagination.

    Prints:
        A sorted count of keywords, or nothing if the subreddit is invalid.
    """
    if counts is None:
        counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    params = {'after': after, 'limit': 100}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    word_list = [word.lower() for word in word_list]

    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        words = re.findall(r'\b\w+\b', title)
        for word in words:
            if word in word_list:
                counts[word] += 1

    after = data.get("data", {}).get("after")
    if after:
        return count_words(subreddit, word_list, counts, after)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")

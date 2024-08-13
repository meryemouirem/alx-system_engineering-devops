#!/usr/bin/python3
"""
this doc is for module
"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def recurse(subreddit, hot_list=[], after=None):
    """
    doc module
    """
    if not subreddit:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    if after:
        url += f"&after={after}"

    response = requests.get(url, allow_redirects=False, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

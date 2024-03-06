#!/usr/bin/python3
""" Function that query the reddit and return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ Gets the number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = ('https://www.reddit.com/r/{}/about.json'.format(subreddit))
    respond = requests.get(url, headers=headers, allow_redirects=False)
    if respond.status_code != 200:
        return 0
    return respond.json().get('data').get('subscribers')

#!/usr/bin/python3
""" Function that query the reddit and return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ Gets the number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    # If the status code is not 200, return 0
    if response.status_code != 404:
        result = response.json().get('data')
        return result.get('subscribers')
    return 0

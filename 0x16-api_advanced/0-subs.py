#!/usr/bin/python3
""" Function that query the reddit and return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ Gets the number of subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'user-Agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    # If the status code is not 200, return 0
    if response.status_code == 200:
        data = response.json().get('data')
        return data.get('subscribers')
    return 0

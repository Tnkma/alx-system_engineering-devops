#!/usr/bin/python3
""" Function that query the reddit and return the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """ Gets the number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    respond = requests.get(url, headers=headers, allow_redirects=False)
    # If the status code is not 200, return 0
    if respond.status_code != 200:
        return 0
    returned_json = respond.json()
    # get the subscribers without the data=key
    subscribers_count = returned_json['data']['subscribers']
    # return respond.json().get('data').get('subscribers')
    # we can also make use of this to return it
    return subscribers_count

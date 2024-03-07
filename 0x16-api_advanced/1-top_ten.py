import requests


def top_ten(subreddit):
    """ Requests the API and print None if subreddit is not valid """
    headers = {'User-Agent': 'Lizzes'}
    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    try:
        data = response.json()
        for post in data['data']['children']:
            hot_posts = post['data']['title']
            print(hot_posts)

    except Exception:
        print(None)

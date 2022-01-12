import json, os
from TwitterAPI import TwitterAPI

api = None


def login(api_key, api_key_secret, access_token, access_token_secret):
    global api
    api = TwitterAPI(api_key, api_key_secret, access_token, access_token_secret)


def get_tweet(tweet_id):
    r = api.request('statuses/lookup', {'id': tweet_id})
    if r.status_code != 200:
        print("Get tweet failed: %s" % r.json()['errors'][0]['message'])
        return None
    print(json.dumps(r.json()[0], indent=4))
    return format_tweet(r.json()[0])


def post(s):
    r = api.request('statuses/update', {'status': s})
    if r.status_code != 200:
        print("Post failed: %s" % r.json()['errors'][0]['message'])
        return None
    return format_tweet(r.json())


def reply(tweet, s):
    s = "@%s %s" % (tweet['user'], s)
    r = api.request('statuses/update', {'status': s, 'in_reply_to_status_id': tweet['id']})
    if r.status_code != 200:
        print("Reply failed: %s" % r.json()['errors'][0]['message'])
        return None
    return format_tweet(r.json())


def retweet(tweet):
    r = api.request('statuses/retweet/:%s' % tweet['id'], {'tweet_id': tweet['id']})
    if r.status_code != 200:
        print("Retweet failed: %s" % r.json()['errors'][0]['message'])
        return None
    return format_tweet(r.json())


def unretweet(tweet):
    r = api.request('statuses/unretweet/:%s' % tweet['id'], {'tweet_id': tweet['id']})
    if r.status_code != 200:
        print("Retweet failed: %s" % r.json()['errors'][0]['message'])
        return None
    return format_tweet(r.json())


def follow(user):
    r = api.request('friendships/create', {'screen_name': "@" + user.strip("@")})
    if r.status_code != 200:
        print("Follow failed: %s" % r.json()['errors'][0]['message'])
        return False
    return True


def unfollow(user):
    r = api.request('friendships/destroy', {'screen_name': "@" + user.strip("@")})
    if r.status_code != 200:
        print("Unfollow failed: %s" % r.json()['errors'][0]['message'])
        return False
    return True


def like(tweet):
    r = api.request('favorites/create', {'id': tweet['id']})
    if r.status_code != 200:
        print("Like failed: %s" % r.json()['errors'][0]['message'])
        return False
    return True


def unlike(tweet):
    r = api.request('favorites/destroy', {'id': tweet['id']})
    if r.status_code != 200:
        print("Unlike failed: %s" % r.json()['errors'][0]['message'])
        return False
    return True


def quote_post(s, tweet):
    r = api.request('statuses/update', {'status': s, 'attachment_url': tweet['url']})
    if r.status_code != 200:
        print("Post failed: %s" % r.json()['errors'][0]['message'])
        return None
    return format_tweet(r.json())


def timeline():
    r = api.request('statuses/home_timeline', {'count': 20})
    if r.status_code != 200:
        print("Request failed: %s" % r.json()['errors'][0]['message'])
        return []
    data = r.json()
    tweets = [format_tweet(tweet) for tweet in data]
    return tweets


def search(q):
    # https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators
    r = api.request('search/tweets', {'q': q + " -filter:retweets", 'count': 5, 'include_entities': True})
    if r.status_code != 200:
        print("Request failed: %s" % r.json()['errors'][0]['message'])
        return []
    data = r.json()
    tweets = [format_tweet(tweet) for tweet in data['statuses']]
    return tweets


def format_tweet(data):
    tweet = {}
    tweet['id'] = data['id_str']
    tweet['text'] = data['text']
    tweet['time'] = data['created_at']
    tweet['user'] = data['user']['screen_name']
    tweet['user_name'] = data['user']['name']
    tweet['user_follows'] = data['user']['friends_count']
    tweet['user_followers'] = data['user']['followers_count']
    tweet['hashtags'] = [hash['text'] for hash in data['entities']['hashtags']]
    tweet['mentions'] = [mention['screen_name'] for mention in data['entities']['user_mentions']]
    tweet['links'] = [url['expanded_url'] for url in data['entities']['urls']]
    tweet['likes'] = data['favorite_count']
    tweet['retweets'] = data['retweet_count']
    tweet['is_quote'] = data['is_quote_status']
    tweet['replies_to'] = data['in_reply_to_status_id_str']
    tweet['url'] = "https://twitter.com/%s/statuses/%s" % (tweet['user'], tweet['id'])
    return tweet


def tprint(tweet):
    print(json.dumps(tweet, indent=4))

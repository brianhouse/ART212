import time
from twitter_functions import *

# @infr4s0und
# l;kahds[982h4uvdfh

api_key = "j6VkHZsqkTzll0cnz9zfzNJtm"
api_key_secret = "7FXWhbilB1NSVksvj9V7iirhn0pHcLLuzSvLpGjoYTw8KAyB4t"
access_token = "1446526046971461634-pYlDkQD4cLkEChDPINgDSsU7ltvvH4"
access_token_secret = "GodS4MDoFHYwTHgfnRvN18jNvbJDSyfVxfpyoa612ltuM"

login(api_key, api_key_secret, access_token, access_token_secret)

# tweet = post("%s #test #teaching https://lclark.edu" % time.time())
# print(tweet)

# tweet = {'id': '1446620831606403072', 'text': '@infr4s0und Thank you', 'time': 'Fri Oct 08 23:37:37 +0000 2021', 'user': 'infr4s0und', 'user_name': 'infr4s0und', 'user_follows': 2, 'user_followers': 0, 'hashtags': [], 'mentions': ['infr4s0und'], 'links': [], 'likes': 0, 'retweets': 0, 'is_quote': False, 'url': 'https://twitter.com/infr4s0und/statuses/1446620831606403072'}

# res = reply(tweet, "You're welcome! ish.")
# print(res)

# tweet = {'id': '1481030155841773578', 'url': 'https://twitter.com/POTUS/status/1481030155841773578'}
#
# res = quote_post("good point", tweet)
# print(res)

# tweets = timeline()
# for tweet in tweets:
#     tprint(tweet)

tweet = get_tweet("1480957453260836866")
tprint(tweet)

# tweets = search("sound")
# for tweet in tweets:
#     tprint(tweet)

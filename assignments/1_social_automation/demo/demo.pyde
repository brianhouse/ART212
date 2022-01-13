from twitter_helper import *

init(SimpleTweet(this))
api_key("");
api_key_secret("");
access_token("");
access_token_secret("");


background(255)
fill(255, 0, 0)
for i in range(10):
    square(random(width), random(height), random(200))

post_image("another")


# tweets = search("fart")

# print(tweets[0])

# list_methods()

# tweet = get_tweet("1432824803761610752")
# print(tweet)

# post("outside")

# tweet = unretweet(tweet)
# print(tweet)

# unfollow("@h0use")

# unlike(tweet)

# tweets = mentions()
# for tweet in tweets:
#     print(tweet)

# t = quote(tweet, "this is the right idea")
# print(t)

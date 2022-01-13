from twitter_helper import *

init(SimpleTweet(this))
api_key("V75SFbPLj9Oe9f0d8wFIq6X9G");
api_key_secret("SdTri0TMiP3fV0tDsVO1GF5tI3ygIyixdXDMrzPGUg2ElrmYen");
access_token("1446526046971461634-FsEvD5O9jLT3ZYE3mU6YiR3Hvdrbmq");
access_token_secret("S4ZV11hA0fFz3affNbsV9kJkYR5UmVnBcvE9RaTSVsmeu");

size(400, 400)

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

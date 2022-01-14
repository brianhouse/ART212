from twitter_helper import *
init(SimpleTweet(this))

api_key("V75SFbPLj9Oe9f0d8wFIq6X9G");
api_key_secret("SdTri0TMiP3fV0tDsVO1GF5tI3ygIyixdXDMrzPGUg2ElrmYen");
access_token("1446526046971461634-FsEvD5O9jLT3ZYE3mU6YiR3Hvdrbmq");
access_token_secret("S4ZV11hA0fFz3affNbsV9kJkYR5UmVnBcvE9RaTSVsmeu");

tweets = search("baadsfasdfgel")
tweet = choice(tweets)
print_tweet(tweet)

reply(tweet, "I like bagels, too!")

# Project #1: Social Automation

Much of the interaction that happens online is not between people, but between people and algorithms, or even between algorithms and algorithms. For example, huge platforms like Facebook, Google, and Twitter are constantly monitoring our activity and manipulating our feeds accordingly—and these platforms provide the environment for third-parties to attempt to game the system. From benign bots that tweet jokes to malicious fake followers that sow disinformation, we're not not alone out there.

For this project, you will create an experimental "Twitter Bot" using code. Your bot will maintain a presence online by automatically posting text and/or images, and it may interact socially by replying to others' comments. It may or may not be apparent to others that your bot is automated.

This is a 3-week project. This week you will present a proposal of your idea to the class for feedback. Next week, you will present your progress. The following week will be a crit. You must have an underlying artistic concept articulated with a 3-sentence artistic statement that you will present with the work.


## Twitter


## Tools

For this project, we'll be writing code in Processing using Python, just like in Digital Media I. If you're new to Processing or have used p5 instead, you may want to [review how to get set up](https://github.com/brianhouse/ART112/blob/master/units/0_algorithm/getting_started.md).

Additionally, we're going to need to need to add some library code in order to interface with Twitter's API. API stands for Application Programming Interface, and it's a way that your computer will communication with Twitter's servers in order to control your bot without using the normal web interface.

Finally, we're going to add some files to our Processing sketch before we begin. First, open a new sketch, and save it. Then, to add files, remember that you can use Processing's "Add File..." menu option:
<p align="center">
  <img src="img/add_file.png" width=200 />
</p>

The first two files to add will allow us to access the Twitter API. Download each of these and add them to your sketch (click "raw" on the next page, and then save the file):
- [simpletweet.jar](social_automation_demo/code/simpletweet.jar)
- [twitter4j-core-4.0.7.jar](social_automation_demo/code/twitter4j-core-4.0.7.jar)

Next, we'll include some code that I've written to help us get up and running faster. Download this and add it to your sketch:
- [twitter_helper.py](social_automation_demo/twitter_helper.py)

Finally, you may need some word lists. Download each of these and add them to your sketch:
- [list_stop_words.txt](social_automation_demo/data/list_stop_words.txt)
- [list_adjectives.txt](social_automation_demo/data/list_adjectives.txt)
- [list_interjections.txt](social_automation_demo/data/list_interjections.txt)
- [list_nouns.txt](social_automation_demo/data/list_nouns.txt)
- [list_prepositions.txt](social_automation_demo/data/list_prepositions.txt)
- [list_pronouns.txt](social_automation_demo/data/list_pronouns.txt)
- [list_verbs.txt](social_automation_demo/data/list_verbs.txt)

(We will be working with language in ways similar to the "Recombination" unit in Digital Media I. You can review that [here](https://github.com/brianhouse/ART112/blob/master/units/5_recombination/code.md), and you may want to also include "word_helper.py" from that unit if you want to do more advanced operations.)

Download and add each of these files to your sketch.

Once all of these files are in place, type these lines into your sketch, save it, and then run:

```py
from twitter_functions import *
init(SimpleTweet(this))

```
You should see the output:
```
Successfully loaded Twitter API
```
If you get an error instead, get help and we'll figure it out.


## Getting set up with Twitter

You'll need a [Twitter](https://twitter.com) account (even if you already have one, create a new one for this project). Sign up using your lclark.edu email address by clicking the "Sign up with Google" option. The Twitter handle you choose will be the name of your bot. Choose something now, but don't worry, you can change it later.

After you create an account, send me the handle so I can add you to our developer team. You should then receive an invite in your email. Accept the invite—you'll have to agree to terms and conditions, and then you'll be taken to the [Twitter developer portal](https://developer.twitter.com/en/portal/dashboard).

Next, you'll create a "Standalone App":

<p align="center">
  <img src="img/create_app.png" width=600 />
</p>

Give your app a name:

<p align="center">
  <img src="img/name_app.png" width=600 />
</p>

Click next, and you'll be shown a screen with some long key strings. We'll need to use the "API Key" and the "API Key Secret" in our program. Copy these two strings and paste them into your sketch as shown:

<p align="center">
  <img src="img/keys.png" width=600 />
</p>

```py
from twitter_helper import *
init(SimpleTweet(this))

api_key("XXXXXXXXXXXXXXXXXXXXXXXXX")
api_key_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
```


After continuing to settings, and scroll down to "App Permissions". We need to change this to "Read and Write" in order to post tweets with our bots. Go ahead and make that change and save it:


<p align="center">
  <img src="img/app_permissions_1.png" width=600 />
</p>

<p align="center">
  <img src="img/app_permissions_2.png" width=600 />
</p>

Next, go to the tab "Keys and tokens". Under the "Authentication Tokens" section will be a button to generate an "Access Token and Secret":

<p align="center">
  <img src="img/generate_access_token.png" width=600 />
</p>

Click "Generate":

<p align="center">
  <img src="img/access_token.png" width=600 />
</p>

```py
from twitter_helper import *
init(SimpleTweet(this))

api_key("XXXXXXXXXXXXXXXXXXXXXXXXX")
api_key_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
```

Once you've copied and pasted these strings into new variables in your sketch, go ahead and click "Yes, I saved them."

All of these settings and "tokens" and "secrets" are security measures to make sure that the app you're going to write is indeed authorized to make posts to Twitter and not some malicious virus taking over your account. It's a pain, but it's also important, and APIs other than Twitter will have their own similar procedures for getting set up. However, if all goes well here, we won't need to access any of this stuff again.


## Interfacing with Twitter

### Tweeting

Now that we have everything set up—phew—we're ready to post a tweet:

```py
from twitter_helper import *
init(SimpleTweet(this))

api_key("XXXXXXXXXXXXXXXXXXXXXXXXX")
api_key_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

post("Hello World!")
```
If you look at your bot's Twitter account, you should see the tweet. Congratulations, you've made a Twitter bot!

### Searching

Next, let's do a search for recent tweets about ... bagels.
```py
# From now on, the examples won't include the setup lines
# that always go at the beginning of your sketch

tweets = search("bagel")
```
This line will search for recent tweets that include the term "bagel" and return a list of tweets.

To see how many, we can use `len` to get the length of the list, and `print` to print it to the console:
```py
tweets = search("bagel")
print(len(tweets))
```
```
100
```
So we have a list of 100 tweets. To take a closer look at one, we can use the random `choice()` function as well as a special function called `print_tweet()` that will make things more legible:
```py
tweets = search("bagel")
tweet = choice(tweets)
print_tweet(tweet)
```
```
{
    "hashtags": [],
    "user_name": "Bagel",
    "url": "https://twitter.com/BagelBot_/statuses/1481756975230717953",
    "user_followers": 59,
    "is_quote": null,
    "user_follows": 46,
    "mentions": [],
    "replies_to": null,
    "links": [],
    "id": "1481756975230717953",
    "text": "can i eat a bagel even though thats cannibalism because im a bagel",
    "time": "Thu Jan 13 14:36:07 PST 2022",
    "retweets": 0,
    "user": "BagelBot_",
    "likes": 0
}
```
As you can see, a "tweet" is actually a dictionary with all kinds of different fields that are metadata about the tweet itself, including the number of likes and the account of the person who tweeted it (if you copy and paste the "url" into a browser, you can see how it looks on Twitter itself).

(Remember, to work with any of these dictionary fields in your code, you can write something like `tweet['likes']`, for example.)

### Likes and Retweets

Speaking of likes (or favorites, whatever), let's like a tweet:
```py
tweets = search("bagel")
tweet = choice(tweets)
print_tweet(tweet)

like(tweet)
```
If we go online and look at our bot's Twitter account under likes, we'll see this random tweet that our bot has liked. Nice!

What about a retweet?
```py
tweets = search("bagel")
tweet = choice(tweets)
print_tweet(tweet)

retweet(tweet)
```

Now, the tweet will show up on our bot's feed.

### Advanced tweets: Replies and Quotes

To raise the stakes a bit, let's reply to a tweet:
```py
tweets = search("bagel")
tweet = choice(tweets)
print_tweet(tweet)

reply(tweet, "I like bagels, too!")
```

This is an inane and harmless response, but remember that this code has real-world consequences. Somewhere, someone has just received a notification about what our bot has said. This is different than simply coding on our own machines!

We can also do a "quote tweet" which is a tweet of our own, not a retweet, but which references another:
```py
tweets = search("bagel")
tweet = choice(tweets)
print_tweet(tweet)

quote(tweet, "I like bagels, too!")
```

### Following and the Timeline

To follow a user, we need their screen name. We can get that from a tweet, like this:
```py
tweets = search("bagel")
tweet = choice(tweets)
print_tweet(tweet)

user = tweet['user']
follow(user)
```

Once we're following a few people, we can pull the recent tweets from all of them, aka the "timeline", like this:

```py
tweets = timeline()
for tweet in tweets:
    print_tweet(tweet)
```

Notice how we've used the `for item in list` loop format to iterate through all of the tweets on our timeline and print them to the console.

Additionally, we may want to see who we're following. Do this like

### Posting images


### Get tweet


### Time

Rate limiting
https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits

### Putting it together

Here's a bot that follows people that are interested in douglas fir trees, for example. We'd first do a search for "douglas fir", and then follow all of those people.



## References

Examples of artist-made bots:
- [Darius Kazemi](http://tinysubversions.com)
    - https://twitter.com/BodegaBot
    - https://twitter.com/moonshotbot
    - https://twitter.com/WhichOneBot
    - https://twitter.com/rapnamebot
    - https://twitter.com/EatenBot
- [Everest Pipkin](https://everest-pipkin.com) and Loren Schmidt, [Moth Generator](https://twitter.com/mothgenerator)
- Allison Parrish, [Deep Question Bot](https://twitter.com/deepquestionbot)
- [Ramsey Nasser](https://nas.sr), [_Top Gun 555µhz_](https://nas.sr/555µhz/)
- [Constant Dullart](https://www.constantdullaart.com/), [_The Possibility of Raising an Army_](http://army.cheap), article in the [Guardian](https://www.theguardian.com/artanddesign/2015/nov/09/army-for-hire-the-artist-employing-ghost-soldiers-to-invade-facebook-constant-dullaart)
- Brian House and [Kyle McDonald](http://kylemcdonald.net), [_Conversnitch_](https://brianhouse.net/works/conversnitch/)
- https://twitter.com/greatartbot
- https://twitter.com/tinycarebot
- https://twitter.com/infinite_scream


Artist writing about how to make a good bot:
- Harry Josephine Giles, "[Some Strategies of Bot Poetics](https://harryjosephine.com/2016/04/06/some-strategies-of-bot-poetics/)"
- Darius Kazemi, "[Basic Twitter Bot Etiquette](http://tinysubversions.com/2013/03/basic-twitter-bot-etiquette/)"

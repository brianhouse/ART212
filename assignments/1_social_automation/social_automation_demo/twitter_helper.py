from gohai.simpletweet import SimpleTweet
import twitter4j.Query as Query
import twitter4j.QueryResult as QueryResult
import twitter4j.Status as Status
import twitter4j.StatusUpdate as StatusUpdate
import twitter4j.TwitterException as TwitterException
import twitter4j.User as User
import json
from random import choice as rand_choice


api = None
user = None

def init(o):
    global api, user
    api = o
    print("Successfully loaded Twitter API")
    
def api_key(s):
    api.setOAuthConsumerKey(s)

def api_key_secret(s):
    api.setOAuthConsumerSecret(s)
    
def access_token(s):
    api.setOAuthAccessToken(s)
    
def access_token_secret(s):
    api.setOAuthAccessTokenSecret(s)

def get_tweet(tweet_id):
    try:
        tweets = api.twitter.lookup(int(tweet_id))
    except TwitterException as e:        
        print("Error: " + e.getErrorMessage())
        return None
    else:
        return format_tweet(tweets[0]) if tweets else None

def post(s):
    try:
        tweet = api.twitter.updateStatus(s)
    except TwitterException as e:        
        print("Error: " + e.getErrorMessage())    
    else:    
        print("Tweeted " + str(tweet.getId()))

def post_image(s):
    try:
        tweet = api.tweetImage(get(), s)
    except TwitterException as e:        
        print("Error: " + e.getErrorMessage())
    else:
        print("Tweeted")

def reply(tweet, s):
    if tweet is None:
        return
    try:
        s = "@%s %s" % (tweet['user'], s)
        update = StatusUpdate(s)
        update.setInReplyToStatusId(int(tweet['id']))
        tweet = api.twitter.updateStatus(update)
    except TwitterException as e:        
        print("Error: " + e.getErrorMessage())
    else:
        print("Tweeted " + str(tweet.getId()))
    
def retweet(tweet):
    try:
        tweet = api.twitter.retweetStatus(int(tweet['id']))
    except TwitterException as e:        
        print("Error: " + e.getErrorMessage())
    else:
        print('Retweeted ' + str(tweet.getId()))

def unretweet(tweet):
    try:
        tweet = api.twitter.unRetweetStatus(int(tweet['id']))
    except TwitterException as e:      
        print("Error: " + e.getErrorMessage())
    else:
        print('Unretweeted ' + str(tweet.getId()))
    
def follow(user):
    try:
        result = api.twitter.createFriendship("@" + user.strip("@"))
    except TwitterException as e:      
        print("Error: " + e.getErrorMessage())    
    else:
        print('Followed user @' + user)
    
def unfollow(user):
    try:
        result = api.twitter.destroyFriendship("@" + user.strip("@"))
    except TwitterException as e:      
        print("Error: " + e.getErrorMessage())    
    else:
        print('Unfollowed user @' + user)        

def like(tweet):
    try:
        result = api.twitter.createFavorite(int(tweet['id']))
    except TwitterException as e:      
        print("Error: " + e.getErrorMessage()) 
    else:   
        print('Liked ' + str(result.getId())) 

def unlike(tweet):
    try:
        result = api.twitter.destroyFavorite(int(tweet['id']))
    except TwitterException as e:      
        print("Error: " + e.getErrorMessage())
    else:
        print('Unliked ' + str(result.getId())) 
                                                                                                    
def quote(tweet, s):
    try:
        update = StatusUpdate(s)
        update.setAttachmentUrl(tweet['url'])
        tweet = api.twitter.updateStatus(update)
    except TwitterException as e:        
        print("Error: " + e.getErrorMessage())
    else:        
        print('Quoted ' + str(tweet.getId()))    
                                    
def timeline():
    try:
        tweets = api.twitter.getHomeTimeline()
        tweets = [format_tweet(tweet) for tweet in tweets]
    except TwitterException as e:        
        print("Error: " + e.getErrorMessage())        
        return []        
    else:
        return tweets    

def mentions():
    try:
        tweets = api.twitter.getMentionsTimeline()
        tweets = [format_tweet(tweet) for tweet in tweets]
    except TwitterException as e:        
        print("Error: " + e.getErrorMessage())                
        return []    
    else:
        return tweets                                        
                      
# def get_followed():
#     friends = []
#     while True:
#         cur = -1
#         result = api.twitter.getFriendsIDs(cur)
#         print(result)
#         for id in result.getIDs():
#             friends.append(int(id))
#         cur = result.getNextCursor()
#         if result == 0:
#             break    
#         break
#     print(friends)                        

def list_methods():
    for item in dir(api.twitter):
        print(item)


def search(term):
    try:
        query = Query(term)
        query.setCount(100)
        tweets = api.twitter.search(query).getTweets()
        tweets = [format_tweet(tweet) for tweet in tweets]
    except TwitterException as e:        
        print("Error: " + e.getErrorMessage())        
        return []                
    else:
        return tweets
    
    
def format_tweet(data):
    # https://twitter4j.org/javadoc/twitter4j/Status.html
    if (data is None) or (type(data) is not dict) or ('id' not in data):
        print('{}')
        return
    try:
        tweet = {}
        tweet['id'] = str(data.getId())
        tweet['text'] = data.getText()
        tweet['time'] = data.getCreatedAt()
        user = data.getUser()
        tweet['user'] = user.getScreenName()
        tweet['user_name'] = user.getName()
        tweet['user_follows'] = user.getFriendsCount()
        tweet['user_followers'] = user.getFollowersCount()
        tweet['hashtags'] = [hash.getText() for hash in data.getHashtagEntities()]
        tweet['mentions'] = [mention.getScreenName() for mention in data.getUserMentionEntities()]
        tweet['links'] = [url.getExpandedURL() for url in data.getURLEntities()]
        tweet['likes'] = data.getFavoriteCount()
        tweet['retweets'] = data.getRetweetCount()
        quote = data.getQuotedStatus()
        tweet['is_quote'] = True if quote is not None else False
        tweet['replies_to'] = data.getInReplyToScreenName()
        tweet['url'] = "https://twitter.com/%s/statuses/%s" % (tweet['user'], tweet['id'])
        return tweet
    except (Exception, TwitterException) as e:
        print(e)    

def print_tweet(tweet):
    print(json.dumps(tweet, indent=4, sort_keys=True, ensure_ascii=False, default=lambda o: unicode(o)))


def choice(l):
    try:
        return rand_choice(l)
    except IndexError:
        print("No items to choose from!")
        return None

# http://www.java2s.com/example/java-api/twitter4j/twitter/index.html

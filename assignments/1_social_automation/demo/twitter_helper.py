from gohai.simpletweet import SimpleTweet
import twitter4j.Query as Query
import twitter4j.QueryResult as QueryResult
import twitter4j.Status as Status
import twitter4j.StatusUpdate as StatusUpdate
import twitter4j.TwitterException as TwitterException
import twitter4j.User as User

api = None

def init(o):
    global api
    api = o
    
def api_key(s):
    api.setOAuthConsumerKey(s);

def api_key_secret(s):
    api.setOAuthConsumerSecret(s);
    
def access_token(s):
    api.setOAuthAccessToken(s);
    
def access_token_secret(s):
    api.setOAuthAccessTokenSecret(s);

def get_tweet(tweet_id):
    tweets = api.twitter.lookup(int(tweet_id))
    return format_tweet(tweets[0]) if tweets else None

def post(s):
    tweet = api.twitter.updateStatus(s)
    return format_tweet(tweet) if tweet else None

def post_image(s):
    tweet = api.tweetImage(get(), s)
    return True

def reply(tweet, s):
    s = "@%s %s" % (tweet['user'], s)
    update = StatusUpdate(s)
    update.setInReplyToStatusId(int(tweet['id']))
    tweet = api.twitter.updateStatus(update)
    return format_tweet(tweet) if tweet else None
    
def retweet(tweet):
    tweet = api.twitter.retweetStatus(int(tweet['id']))
    return format_tweet(tweet) if tweet else None

def unretweet(tweet):
    tweet = api.twitter.unRetweetStatus(int(tweet['id']))
    return format_tweet(tweet) if tweet else None
    
def follow(user):
    result = api.twitter.createFriendship("@" + user.strip("@"))
    return True
    
def unfollow(user):
    result = api.twitter.destroyFriendship("@" + user.strip("@"))
    return True

def like(tweet):
    result = api.twitter.createFavorite(int(tweet['id']))
    return True 

def unlike(tweet):
    result = api.twitter.destroyFavorite(int(tweet['id']))
    return True                                                                         
                                                                                                    
def quote(tweet, s):
    update = StatusUpdate(s)
    for item in dir(update):
        print(item)
    update.setAttachmentUrl(tweet['url'])
    tweet = api.twitter.updateStatus(update)
    return format_tweet(tweet) if tweet else None
                                    
def timeline():
    tweets = api.twitter.getHomeTimeline()
    tweets = [format_tweet(tweet) for tweet in tweets]
    return tweets    

def mentions():
    tweets = api.twitter.getMentionsTimeline()
    tweets = [format_tweet(tweet) for tweet in tweets]
    return tweets                                        
                                                                                                            
def list_methods():
    for item in dir(api.twitter):
        print(item)


def search(term):
    query = Query(term)
    query.setCount(100)
    tweets = api.twitter.search(query).getTweets()
    tweets = [format_tweet(tweet) for tweet in tweets]
    return tweets
    
    
def format_tweet(data):
    # https://twitter4j.org/javadoc/twitter4j/Status.html
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
    tweet['is_quote'] = format_tweet(quote) if quote is not None else None
    tweet['replies_to'] = data.getInReplyToScreenName()
    tweet['url'] = "https://twitter.com/%s/statuses/%s" % (tweet['user'], tweet['id'])
    return tweet    

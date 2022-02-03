from twitter_helper import *
init(SimpleTweet(this))

api_key("XXXXXXXXXXXXXXXXXXXXXXXXX")
api_key_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

size(640, 480)
        
def run():        
    # search for tweets
    tweets = search("#pizza OR #bagels")
    
    # get a list of the tweets that have images 
    tweets_with_images = []    
    for tweet in tweets:
        if tweet['image'] is not None:
            tweets_with_images.append(tweet)
            
    # pick one
    tweet = choice(tweets_with_images)
                                    
    # load the image from twitter
    source = loadImage(tweet['image'])
    
    # resize the image so it fills your canvas
    source.resize(width, height)

    # glitch away
    # https://github.com/brianhouse/ART112/blob/master/units/6_glitch/code.md
    background(0)
    offset = 50
    for y in range(height):
        for x in range(width):    
            pixel_1 = source.get(x, y)
            r_1 = red(pixel_1)
            g_1 = green(pixel_1)
            b_1 = blue(pixel_1)    
            pixel_2 = source.get(x + offset, y)
            r_2 = red(pixel_2)
            g_2 = green(pixel_2)
            b_2 = blue(pixel_2)    
            stroke(r_1, g_2, b_2)   
            point(x, y)     
                
    # (alternately, you can just show the image)
    # image(source, 0, 0)
    
    # post to twitter
    post_image("This is my glitch version")
        
run()        

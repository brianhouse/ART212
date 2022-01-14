from twitter_helper import *
init(SimpleTweet(this))

api_key("XXXXXXXXXXXXXXXXXXXXXXXXX")
api_key_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

size(400, 400)

def run():
    for i in range(20):
        color(random(255), random(255), random(255))
        square(random(400), random(400), random(200))    
    post_image("A new generative drawing")
        
while True:
    run()
    time.sleep(10*60) # 10 minutes * 60 seconds per minute

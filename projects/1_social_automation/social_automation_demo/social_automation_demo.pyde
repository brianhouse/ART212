from twitter_helper import *
init(SimpleTweet(this))

api_key("XXXXXXXXXXXXXXXXXXXXXXXXX")
api_key_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

# size(400, 400)

# def run():
#     for i in range(20):
#         color(random(255), random(255), random(255))
#         square(random(400), random(400), random(200))    
#     post_image("A new generative drawing")
        
# while True:
#     run()
#     time.sleep(10*60) # 10 minutes * 60 seconds per minute


nouns = open("list_nouns.txt").read().split()
adjectives = open("list_nouns.txt").read().split()
imperatives = open("list_verbs_imperative.txt").read().split()
past = open("list_verbs_past.txt").read().split()
interjections = open("list_interjections.txt").read().split()

print("")
text = choice(interjections).title() + "! The " + choice(nouns) + " has " + choice(past) + " the " + choice(nouns) + "!"
print(text)

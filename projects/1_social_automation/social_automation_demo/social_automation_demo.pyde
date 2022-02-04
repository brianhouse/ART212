from twitter_helper import *
init(SimpleTweet(this))

api_key("XXXXXXXXXXXXXXXXXXXXXXXXX")
api_key_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
access_token_secret("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")



def translate(q, lang):
    import urllib, urllib2, json
    # For language codes, see https://sites.google.com/site/opti365/translate_codes
    TRANSLATE_KEY = "AIzaSyAtvQwuows2WiV9nJ2kawF2p4wS_YpgKG4"
    try:
        url = "https://translation.googleapis.com/language/translate/v2?key=" + TRANSLATE_KEY + "&q=" + urllib.quote_plus(q) + "&target=" + lang
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        result = json.loads(response.read())
        return result['data']['translations'][0]['translatedText']
    except Exception as e:
        print(e)
        return None
    

result = translate("My name is Brian", "vi")
print(result)

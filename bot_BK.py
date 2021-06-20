import tweepy
import random

API_KEY = "TsDC5eideARsqYRokOqWXknx2"
API_SECRET = "cTq3mcE4lsFl9RgMSsz43E4IAY8nOQziuD17u8vjyCtgdnITHI"

ACCESS_TOKEN = "1401540013125509125-z1X4CC7syvXdmFXOWwNI1RDFR3J6d4"
ACCESS_TOKEN_SECRET = "jCxAoje3AMsOuqK5WIlNnI5fyoGIrSo62snd26TEBHOpE"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)




number= random.randint(1,10000000)
try:
    api.update_status(str(number)+' @BurgerKingFR',in_reply_to_status_id=1405819904071249928)
except:
    None



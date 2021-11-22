import tweepy
from random import randint
import time


def selectfollow(texte):
    check=True
    listeresult=[]
    for i in texte:
        if i!='@' and check:
            chaine=''
        else:
            check=False
            chaine+=i
            if i==' ':
                check=True
                chaine=chaine[1:-1]
                listeresult.append(chaine)
    return listeresult



def tweetopif(api):
    #global listetr
    
    trendsalea=api.trends_place(23424819)[0]['trends'][randint(0,10)]['name']
    query = trendsalea
    max_tweets = 1000
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
    listetr=[]
    for i in searched_tweets:
        if i.text[0]+i.text[1]!='RT' and i.in_reply_to_status_id==None and i.lang=='fr' and len(i.text)<114:         #searched_tweets[0].id
            listetr.append(i)
    if len(listetr)-1>=0:
        api.update_status(listetr[randint(0,len(listetr)-1)].text)
        print(listetr[0].text)
    

    

            
#Pjactare  Pepssi19 kriterre  Huam52524437

#StephNulos  guyonnathalie1
#Alexispouillat1 (pas très actif)

def routine(tweet):
    api.retweet(tweet.id)
    tweet.favorite()
    #listefollow=selectfollow(tweet.text)
    api.update_status("@Pjactare @Pepssi19 @kriterre @Huam52524437 @"+str(tweet.author.screen_name),in_reply_to_status_id=tweet.id)
    print('ok')
    #listetr[0].author.name
    api.create_friendship(tweet.author.id)
    

    
#AAAAAAAAAAAAAAAAAAAAACXKSAEAAAAAEX2Ep0owNdU17Pu5vmli2e7XUwk%3DdHHfOnlLIOVZ9yC2NQ88oYwaababPLJHNQPtJkXe6OXFbjwPFr

API_KEY = "c9kZwmrgvoxKpGICSdlZ1GyFy"
API_SECRET = "gja0kY0muSYuDXHKFEe4v2UIaxvT9KcVzNcsH9lnR8IfVcrD5P"

ACCESS_TOKEN = "1401540013125509125-8sxK8sR6tRjyrnC16oo5QwglDMBP7F"
ACCESS_TOKEN_SECRET = "LN0PKsj07o7h4UdIDNdEUqmV3j2YKUfANZ03YPyF5q1Z7"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

listerep=["Regardez-ca","Ca a l'air cool","Wahh", "Je participe"]


api = tweepy.API(auth)

# pour chercher les tendances
###api.trends_place(23424819)[0]['trends'][49]['name']

while True:  
    query = 'giveaway'
    max_tweets = 200
    verif=True
    while verif:
        try:
            searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
            verif=False
        except:
            print('erreur')
            time.sleep(20)
            


    listetr=[]
    ##while len(listetr)<1:
    ##    max_tweets += 10
    ##    searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
    ##    listetr=[]
    ##    for i in searched_tweets:
    ##        if i.text[0]+i.text[1]!='RT' and i.in_reply_to_status_id!=None:         #searched_tweets[0].id
    ##            listetr.append(i)
    ##            print('\n\n-----------------------------------------------\n'+i.text)


    for i in searched_tweets:
        if i.text[0]+i.text[1]!='RT' and i.in_reply_to_status_id==None:         #searched_tweets[0].id
            listetr.append(i)
            #print('\n\n-----------------------------------------------\n'+i.text)

    try:
        query = 'concours'
        max_tweets = 100
        searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
        for i in searched_tweets:
            if i.text[0]+i.text[1]!='RT' and i.in_reply_to_status_id==None:         #searched_tweets[0].id
                listetr.append(i)
                #print('\n\n-----------------------------------------------\n'+i.text)

    except:
        None
        

    try:
        query = 'concours paypal'
        max_tweets = 100
        searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

        for i in searched_tweets:
            if i.text[0]+i.text[1]!='RT' and i.in_reply_to_status_id==None:         #searched_tweets[0].id
                listetr.append(i)
                #print('\n\n-----------------------------------------------\n'+i.text)
    except:
        None

    for i,j in enumerate(listetr):
        if i%5==0:
            verif=True
            while verif:
                try:
                    tweetopif(api)
                    verif=False
                except:
                    print('erreur tweet')
                    time.sleep(20)
        try:
            routine(j)
        except:
            None
        time.sleep(36)

    time.sleep(1200)

#api.update_status('Test',in_reply_to_status_id=1406609822460559361)

            


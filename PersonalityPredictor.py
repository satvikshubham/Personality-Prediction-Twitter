from itertools import count
from config import *
import tweepy
import datetime
import pandas as pd
import os


auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)
print("Enter username")
username = input()
query = "from:" + username

tweets_list = tweepy.Cursor(api.search_tweets, q=query,tweet_mode='extended', lang='en').items()

output = []
fLine = ""
for tweet in tweets_list:
    text = tweet._json["full_text"]
    line = {'posts' : text}
    fLine += text + "|||"
    
f = open("tweets.txt", "w",encoding="utf-8")
f.write(fLine)
fLine = {'posts' : fLine}
output.append(fLine)
df = pd.DataFrame(output)
df.to_csv('output.csv')


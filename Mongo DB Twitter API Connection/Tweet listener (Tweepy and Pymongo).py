# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:29:59 2017
@author: Scott
"""
from pymongo import MongoClient
import json
import tweepy

MONGO_HOST = 'mongodb://localhost/twitterdb'  
# assumes you have mongoDB installed locally
# and a database called 'twitterdb'

WORDS = ['#worldseries']
# creates a dictionary of words to listen for

ckey = '...'
consumer_secret = '...'
access_token_key = '...'
access_token_secret = '...'
# ^^ insert your Twitter API keys here 

class StreamListener(tweepy.StreamListener):    
        #This is a class provided by tweepy to access the Twitter Streaming API. 
 
    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        # This connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)
            
            # Use twitterdb database. If it doesn't exist, it will be created.
            db = client.twitterdb
    
            # Decode the JSON from Twitter
            datajson = json.loads(data)
            
            #grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']
 
            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))
            
            #insert the data into the mongoDB into a collection called twitter_search
           
	    #if twitter_search doesn't exist, it will be created.
            db.twitter_search.insert(datajson)
        except Exception as e:
           print(e)

# Creates auth handler and token containing the API info you entered
auth = tweepy.OAuthHandler(ckey, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.

listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)
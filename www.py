import tweepy
import sqlite3
import json

consumer_key = 'zm691mL5UAdVzZ5nNwAWEMjJn'
consumer_secret = '6NYTUi7bHIhqSukYi31Su6ytwT3JoshGTEyZpUMhqyedRoXLjb'
access_token = '1209931045-3eWGEFv9lHs8f5aKfZsKpD1nnXcF2EA83ReNpok'
access_token_secret = 'XRFgWdruf3ZInOtRjmGENi9KM6LsbJ2lVRwZUVk7c7CtN'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

def search_for_words(consumer_key, consumer_secret, access_token, access_token_secret, stock_phrase):

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status)

    def on_error(self, status_code):
        print(status_code)

    def on_data(self, raw_data):
        

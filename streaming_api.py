# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

import os
# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '3043501246-cAtrlTygdncQv3sCRfmnRLxqgNsy8seOjXtrMu4'
ACCESS_SECRET = 'lJygQn4gcqUcbfql2D6NMAVFMStPLiLwQQBiWTKTsd4BA'
CONSUMER_KEY = '7LQZ9AflFNt3xYbAgaP7Pj7J9'
CONSUMER_SECRET = 'SlzzDzp6XUjXbn38CDkF2eh5uJ4H98u5S38IjLzYqz3zkysaYM'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
#iterator = twitter_stream.statuses.sample()
import os
#output filepath for file 
output_filename = os.path.join(os.path.expanduser("~"), "Desktop", "TWITTER API", "data", "streaming_tweets_for_class.json")

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer.
# set to 10 for the time being 
tweet_count = 100
iterator = twitter_stream.statuses.filter(track="Depressed", language="en")
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    
    with open(output_filename, 'a') as output_file:
        output_file.write(json.dumps(tweet['text']))
        output_file.write("\n")
    # dumps tweet info into streaming_tweets.json
    if tweet_count <= 0:
        break

# In[ ]:




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
#output filepath for file scikit-learn//scikit-learn-master//sklearn//twitter_data//
output_filename = os.path.join(os.path.expanduser("~"), "scikit-learn", "scikit-learn-master", "sklearn", "twitter_data", "data", "streaming_tweets.txt")
#create new file path for class
# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer.
# set to 10 for the time being

tweet_count = 100
iterator = twitter_stream.statuses.filter(track="Depressed", language="en")
retweet = 'RT @'
quickClass_filename = os.path.join(os.path.expanduser("~"), "scikit-learn", "scikit-learn-master", "sklearn", "twitter_data", "data", "quickClass_streaming_tweets.txt")
qC = open(quickClass_filename, 'a')
for tweet in iterator:
    #tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
	with open(output_filename, 'a') as output_file:
		if "RT @" not in tweet['text']:
			output_file.write(json.dumps(tweet['user']['id']))
			output_file.write("\t")
			output_file.write(json.dumps(tweet['text']))
			output_file.write("\t")
			output_file.write(json.dumps(tweet['created_at']))
			output_file.write("\n")
			
			qC.write(json.dumps(tweet['user']['id']))
			qC.write("\t")
			qC.write(json.dumps(tweet['text']))
			qC.write("\t")
			qC.write(json.dumps(tweet['created_at']))
			qC.write("\n")

			tweet_count-=1
    # dumps tweet info into streaming_tweets.json
	if tweet_count <= 0:
		break
		
output_file.close()



# In[ ]:



quit


# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json
import numpy as np
import os
# Import the necessary methods from "twitter" library
from twitter import *
import time
# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '3043501246-cAtrlTygdncQv3sCRfmnRLxqgNsy8seOjXtrMu4'
ACCESS_SECRET = 'lJygQn4gcqUcbfql2D6NMAVFMStPLiLwQQBiWTKTsd4BA'
CONSUMER_KEY = '7LQZ9AflFNt3xYbAgaP7Pj7J9'
CONSUMER_SECRET = 'SlzzDzp6XUjXbn38CDkF2eh5uJ4H98u5S38IjLzYqz3zkysaYM'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
input_file = open("/home/bergeron/scikit-learn/scikit-learn-master/sklearn/twitter_data/data/quickClass_streaming_tweets.txt", 'r')
output_filename = os.path.join(os.path.expanduser("~"), "scikit-learn", "scikit-learn-master", "sklearn", "twitter_data", "data", "rest_api_tweets.txt")
twitter = Twitter(auth=oauth)


t = time.strftime("%a %b %d")
quickClass_filename = os.path.join(os.path.expanduser("~"), "scikit-learn", "scikit-learn-master", "sklearn", "twitter_data", "data", "quickClass_rest_tweets.txt")
qC = open(quickClass_filename, 'a')
with input_file as f: #for every line f in streaming file
	for line in f: #for every line in the input file 
		#if t in line: #that contains todays date
		#with open(output_filename, 'a') as output_file: #append original tweet
		#	output_file.write(line)                      #from input file to output file 
		userID = line.split(None,1)[0]  #get user ID from line of input file
		tweets = twitter.statuses.user_timeline(user_id=userID, lang='en', count=20) #search status based on user ID
		counts = 0
		for tweet in tweets: #for every tweet we pulled
			if "RT @" not in tweet['text']: #if the tweet isn't a retweet
				counts+=1
				if counts == 6 :
					break
				with open(output_filename, 'a') as output_file:
					output_file.write(json.dumps(tweet['user']['id']))
					output_file.write("\t")
					qC.write(json.dumps(tweet['user']['id']))
					qC.write("\t")
					output_file.write(json.dumps(tweet['text']))
					output_file.write("\t")
					qC.write(json.dumps(tweet['text']))
					qC.write("\t")
					output_file.write(json.dumps(tweet['created_at']))
					output_file.write("\n")
					qC.write(json.dumps(tweet['created_at']))
					qC.write("\n")
input_file.close()
output_file.close()
qC.close()


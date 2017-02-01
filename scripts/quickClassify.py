import os
# Import the necessary methods from "twitter" library
#from twitter import *
import time
import re
#tTrackFile = open("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//tTrackFile.txt", 'r+')
#fTrackFile = open("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//fTrackFile.txt", 'r+')
#tTrackFile.read()
#fTrackFile.read()
tupTo = input("Enter number of true tweets collected so far: ")
fupTo = input("Enter number of false tweets collected so far: ")
tsi = int(tupTo)
fsi = int(fupTo)
def tstreamIndex():
	global tsi
	tsi = tsi+1
	#return tsi
def fstreamIndex():
	global fsi
	fsi = fsi+1
	#return fsi


def clearDups(filename):
	lines = open(filename, 'r').readlines()
	lines_set = set(lines)
	out  = open(filename, 'w')
	for line in lines_set:
		print(line)
	out.writelines(sorted(lines_set))
	out.close()


def stripSaveText(line,streamind,restind,classif): #sends single tweet to learning classification folder depending on user input (classif = t if depressed or f if not)
	ID = line.split('\t',2)[0]
	text = re.sub(r'[^a-zA-Z ,\']+', " ", (re.sub(r'\bhttp\S+', '', (line.split('\t',2)[1]))))
	date = line.split('\t',2)[2]
	
	if classif == 't':
		log = open('//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//tidLogFile.txt', 'a')
		output_filename = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//tData//tLearnWord//"+str(streamind)+"."+str(restind)+".txt"
		out = open(output_filename, 'w')
		out.write(text)
		out.close()
		log.write(str(streamind)+"."+str(restind)+'\t'+ID+'\t'+date)
		log.close()
	elif classif == 'f':
		log = open('//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//fidLogFile.txt', 'a')
		output_filename = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//tData//fLearnWord//"+str(streamind)+"."+str(restind)+".txt"
		out = open(output_filename, 'w')
		out.write(text)
		out.close()
		log.write(str(streamind)+"."+str(restind)+'\t'+ID+'\t'+date)
		log.close()
	return
	
def sendRest(ID,index,classif):
	restIndex = 0
	restAPI_filename = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//quickClass_rest_tweets.txt"
	restAPI_file = open(restAPI_filename, 'r')
	lines = set(restAPI_file.readlines())
	if classif == 't':
		output_file = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//true_learning_set_tweets.txt"
		#tstreamIndex()
		streamIndex = tsi
	elif classif == 'f':
		output_file = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//false_learning_set_tweets.txt"
		#fstreamIndex()
		streamIndex = fsi
	out = open(output_file, 'a')
	#with restAPI_file as input_file:
	for line in lines:
		if str(ID) not in line:
			continue
		else:
			line_ID = line.split('\t',2)[0]
			restIndex+=1
			out.write(line)
			stripSaveText(line,streamIndex,restIndex,classif)
	out.close()
	restAPI_file.close()
	return


		

#main

streaming_filename = "//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//quickClass_streaming_tweets.txt"
inp = open(streaming_filename, 'r')
with inp as infile:
	for line in infile:
		classif = input(line)
		ID = line.split('\t',2)[0]
		if classif == 't':
			o_file = open("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//true_learning_set_tweets.txt", 'a')
			tstreamIndex()
			stripSaveText(line,tsi,0,classif)
			o_file.write("Streaming:	"+line)
			sendRest(ID,tstreamIndex,classif)
			
		elif classif == 'f':
			o_file = open("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//false_learning_set_tweets.txt", 'a')
			fstreamIndex()
			stripSaveText(line,fsi,0,classif)
			o_file.write("Streaming:	"+line)
			sendRest(ID,fstreamIndex,classif)
#keep track of number of tweets for tData labels and the ID log files
#tTrackFile.write(tstreamIndex)
#fTrackFile.write(fstreamIndex)
#close up
#tTrackFile.close()
#fTrackFile.close()
inp.close()
clearDups("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//true_learning_set_tweets.txt")
clearDups("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//false_learning_set_tweets.txt")
commandClear = input("All done? Double checked? Clear files? (y/n)")
if commandClear == 'y' or commandClear == 'Y':
	os.remove("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//quickClass_streaming_tweets.txt")
	os.remove("//home//bergeron//scikit-learn//scikit-learn-master//sklearn//twitter_data//data//quickClass_rest_tweets.txt")
else:
		print("Ok, bye.")
		
		
	
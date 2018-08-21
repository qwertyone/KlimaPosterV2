# -*- coding: UTF-8 -*-
consumer_key = 'kMlTus7CpLPQ9EGHb5E8A8L2B'
consumer_secret = 'yXCXdlxaqXP1LQ9J9MEXiUumQD63zSR7YzDqvCPCuemUXZgQBr'
access_token = '890596296058425344-2sWcKo7ruUXzcwUzG5DGsDLLxrjPSqH'
access_secret = 'kxFqYAnGxlFvPHpHCmUvbBwowQtvoG7DHsffVi6DQZp8E'

def tweetHeat(indexHeatState, direction, tipHI):
	from twython import Twython,TwythonError
	twitter = Twython(consumer_key, consumer_secret, access_token, access_secret)

	try:
		twitter.update_status(status = '#Karlsruhe #Heat is ' + indexHeatState + ': '+ direction + ' ' + tipHI)
			
	except TwythonError as e:
		print e

def tweetAQI(currentStateAQI,resultAQI,tipAQI):
	from twython import Twython,TwythonError
	twitter = Twython(consumer_key, consumer_secret, access_token, access_secret)

	try:
		twitter.update_status(status = '#Karlsruhe #airQuality is ' + currentStateAQI + ' (' + str(resultAQI) + '). ' + tipAQI)
			
	except TwythonError as e:
		print e

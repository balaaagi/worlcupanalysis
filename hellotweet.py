import tweepy
import json
from tweepy import Stream
config_params=[]
config_params=file('config.txt').read().split()

class MyStreamListener(tweepy.StreamListener):
	def on_status(self,status):
		print status.text
		return True

	def on_error(self,status):
		print status



mystreamListener=MyStreamListener()



auth=tweepy.OAuthHandler(config_params[0],config_params[1])
auth.set_access_token(config_params[2],config_params[3])
api=tweepy.API(auth)

myStream=Stream(auth,mystreamListener)

myStream.filter(track=['sachin'])

#public_tweets=api.user_timeline('balaaagi',count=70)
# user=api.get_user('twitter')

# print "############"
# print user.screen_name
# print user.followers.count
# i=1;
# print "############"
# for tweet in public_tweets:
# 	i=i+1
# 	print tweet.text

# print "no of tweets",i
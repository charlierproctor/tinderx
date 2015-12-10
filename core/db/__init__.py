from pymongo import MongoClient

class Mongo(object):
	# initialize with a connection to the mongo database
	def __init__(self):
		client = MongoClient()
		self.db = client.tinderx


	# profiles, users models
	from profiles import load_profiles,find_random,find_profile
	from users import find_user,insert_user,like_user,dislike_user
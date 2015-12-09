from pymongo import MongoClient

class Mongo(object):
	# initialize with a connection to the mongo database
	def __init__(self):
		self.client = MongoClient()

	# profiles, users models
	from profiles import profiles
	from users import users
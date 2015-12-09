from pymongo import MongoClient

# connect to mongodb tinderx database
def _db():
	client = MongoClient()
	return client.tinderx

# load profiles from mongodb
def load_profiles(num):
	# grab the profiles collection
	profiles_collection = _db().tinder_profiles

	# find and return *num* profiles
	return profiles_collection.find({}).limit(num)


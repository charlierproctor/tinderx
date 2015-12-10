import random

# grab the tinder_profiles collection from mongodb
def _collection(self):
	return self.db.tinder_profiles

# load *num* profiles
def load_profiles(self,num):
	return _collection(self).find({}).limit(num)

# find a random profile
def find_random(self):
	count = _collection(self).count() 
	return _collection(self).find({})[random.randint(0,count-1)]

# find a profile by tinder username
def find_profile(self,username):
	return _collection(self).find_one({'usr':username})

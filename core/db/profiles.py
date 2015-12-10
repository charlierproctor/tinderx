# grab the tinder_profiles collection from mongodb
def _collection(self):
	return self.db.tinder_profiles

# load *num* profiles
def load_profiles(self,num):
	return _collection(self).find({}).limit(num)

# find a random profile
def find_random(self):
	return _collection(self).aggregate([ {"$sample": { "size": 1 }} ])
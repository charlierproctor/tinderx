# grab the tinder_profiles collection from mongodb
def _collection(self):
	return self.db.tinder_profiles

# load *num* profiles
def load_profiles(self,num):
	return _collection(self).find({}).limit(num)
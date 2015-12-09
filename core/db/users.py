# load users collection from mongodb
def _collection(self):
	return self.db.users

# find a user by facebook id
def find_user(self,fbid):
	return _collection(self).find_one({"fbid": fbid})

# insert a user into the database
def insert_user(self,user):
	return _collection(self).insert_one(user)
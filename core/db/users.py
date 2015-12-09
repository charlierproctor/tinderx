# load users collection from mongodb
def _collection(self):
	return self.db.users

# find a user by facebook id
def find_user(self,fbid):
	return _collection(self).find_one({"fbid": fbid})

# insert a user into the database
def insert_user(self,user):
	return _collection(self).insert_one(user)

# from likes to
def like_user(self,from_user,to_user):
	_collection(self).find_one_and_update({"_id": from_user},{
			'$addToSet': {
				"likes": to_user
			}
		})

# from dislikes to
def dislike_user(self,from_user,to_user):
	_collection(self).find_one_and_update({"_id": from_user},{
			'$addToSet': {
				"dislikes": to_user
			}
		})
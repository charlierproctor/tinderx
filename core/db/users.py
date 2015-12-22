import pickle,bson

# load users collection from mongodb
def _collection(self):
	return self.db.users

# find a user by facebook id
def find_user(self,fbid):
	return _collection(self).find_one({"fbid": fbid})

# insert a user into the database
def insert_user(self,user):
	_id = _collection(self).insert_one(user).inserted_id
	return _collection(self).find_one({"_id": _id})


# from likes to
def like_user(self,from_fbid,to_usr):
	return _collection(self).find_one_and_update({"fbid": from_fbid},{
			'$addToSet': {
				"likes": to_usr
			}
		})

# from dislikes to
def dislike_user(self,from_fbid,to_usr):
	return _collection(self).find_one_and_update({"fbid": from_fbid},{
			'$addToSet': {
				"dislikes": to_usr
			}
		})

# update the img with name *img_name* for the user with the given fbid
def update_img(self,fbid,img_name,img):
	return _collection(self).update_one(
			{'fbid':fbid},
			{
				'$set': {
					img_name: bson.binary.Binary(
						pickle.dumps(img,protocol=bson.binary.OLD_BINARY_SUBTYPE)
					)
				}
			}
		)
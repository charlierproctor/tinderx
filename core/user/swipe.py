from ..db import Mongo

def next_profile(self):
	pass

# dislike
def swipe_left(self,users_fbid):
	db = Mongo()
	
	from_user = db.find_user(self.fbid)["_id"]
	to_user = db.find_user(users_fbid)["_id"]

	return db.dislike_user(from_user,to_user)


# like
def swipe_right(self,users_fbid):
	db = Mongo()
	
	from_user = db.find_user(self.fbid)["_id"]
	to_user = db.find_user(users_fbid)["_id"]

	return db.like_user(from_user,to_user)
from ..db import Mongo

def fetch_profile(self):
	db = Mongo()

	# find who this user likes / dislikes already
	user = db.find_user(self.fbid)
	arr = (user.get("likes") or []) + (user.get("dislikes") or [])

	# find a random user
	res,i = db.find_random(),0
	while (res['usr'] in arr and i < 20):
		res,i = db.find_random(),i+1

	# no luck finding a random user
	if i == 20:
		return False

	# strip out the mongo id
	res.pop("_id", None)

	return res

# swipe on a particular user
def swipe(self,user,direction):
	db = Mongo()

	# like / dislike the user accordingly
	if direction == 'left':
		res = db.dislike_user(self.fbid,user.get('usr'))
	else:
		res = db.like_user(self.fbid,user.get('usr'))

	# strip out the mongo id
	res.pop("_id", None)

	return res

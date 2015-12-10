from ..db import Mongo

def fetch_profile(self):
	db = Mongo()

	# find who this user likes / dislikes already
	user = db.find_user(self.fbid)
	arr = user["likes"] + user["dislikes"]

	print arr

# swipe on a particular user
def swipe(self,user,direction):
	db = Mongo()

	# like / dislike the user accordingly
	if direction == 'left':
		return db.dislike_user(self.fbid,user.get('usr'))
	else:
		return db.like_user(self.fbid,user.get('usr'))

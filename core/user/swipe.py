from ..db import Mongo
from ..profile import Profile
import cv2
from ..errors import NoValidFaces

# predict how a user will swipe on a given image, based on a history of swipes.
def _predict(self,img):
	# calculate the differences between this image and the liked / disliked average
	diff_liked = cv2.subtract(img, self.liked_img)
	diff_disliked = cv2.subtract(img, self.disliked_img)

	# calculate the norms of the differences
	norm_liked = cv2.norm(diff_liked)
	norm_disliked = cv2.norm(diff_disliked)

	# and make the prediction
	return 'like' if norm_liked < norm_disliked else 'dislike'

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

	# create a profile object
	prof = Profile(res)
	try:
		prof.normalize()

		# and make a prediction!
		res['prediction'] = _predict(self,prof.gray)
	except NoValidFaces, e:
		# TODO: probably just don't send the image?
		print e

	return res

# swipe on a particular profile
def swipe(self,profile,direction):
	db = Mongo()

	# like / dislike the profile accordingly
	if direction == 'left':
		res = db.dislike_user(self.fbid,profile.get('usr'))
	else:
		res = db.like_user(self.fbid,profile.get('usr'))

	# create our profile object
	prof = Profile(profile)
	prof.normalize()

	# like this profile
	if direction == 'right':
		name = 'liked_img'
		img = self.liked_img
		weight = len(self.likes)
	
	# dislike this profile
	else:
		name = 'disliked_img'
		img = self.disliked_img
		weight = len(self.dislikes)

	# calculate the new image.
	new_img = cv2.addWeighted(img,weight,prof.gray,1,0)

	# and save it to the database
	db.update_img(self.fbid,name,new_img)

	# strip out the mongo id and the two images.
	res.pop("_id", None)
	res.pop("liked_img", None)
	res.pop("disliked_img", None)

	return res

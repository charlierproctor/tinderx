from ..db import Mongo
from ..profile import Profile
import cv2
import numpy as np

# swipe on a particular profile
def swipe(self,profile,direction,prediction):

	print "*"*20, "PROCESS SWIPE", "*"*20

	db = Mongo()

	# like / dislike the profile accordingly
	if direction == 'left':
		res = db.dislike_user(self.fbid,profile.get('usr'))

		# the prediction was correct
		if prediction == 'dislike':
			db.increment_correct(self.fbid,prediction)
	else:
		res = db.like_user(self.fbid,profile.get('usr'))

		# the prediction was correct
		if prediction == 'like':
			db.increment_correct(self.fbid,prediction)

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

	# calculate the weights
	denom = weight + 1
	alpha = float(weight) / float(denom)
	beta = 1.0 / float(denom)

	# calculate the new image.
	new_img = cv2.addWeighted(img,alpha,prof.gray,beta,0) if (isinstance(img,np.ndarray)) else prof.gray

	# and save it to the database
	db.update_img(self.fbid,name,new_img)

	# strip out the mongo id and the two images.
	res.pop("_id", None)
	res.pop("liked_img", None)
	res.pop("disliked_img", None)

	return res

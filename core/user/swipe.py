from ..db import Mongo
from ..profile import Profile
import cv2
from ..errors import NoValidFaces, NoImageYet, NoProfiles
import numpy as np

# predict how a user will swipe on a given image, based on a history of swipes.
def _predict(self,img):

	# raise an error if we don't have liked / disliked images yet.
	if not isinstance(self.liked_img,np.ndarray):
		raise NoImageYet('liked_img')
	elif not isinstance(self.disliked_img,np.ndarray):
		raise NoImageYet('disliked_img')

	# calculate the differences between this image and the liked / disliked average
	diff_liked = cv2.subtract(img, self.liked_img)
	diff_disliked = cv2.subtract(img, self.disliked_img)

	# calculate the norms of the differences
	norm_liked = cv2.norm(diff_liked)
	norm_disliked = cv2.norm(diff_disliked)

	print "liked:", norm_liked 
	print "disliked:", norm_disliked

	# and make the prediction
	return 'like' if norm_liked < norm_disliked else 'dislike'

# return the statistics for this user
def stats(self):
	return {
		'likes': len(self.likes), 
		'dislikes': len(self.dislikes), 
		'like_correct': self.like_correct,
		'dislike_correct': self.dislike_correct
	}

def fetch_profile(self):
	
	print "*"*20, "FETCH NEXT PROFILE", "*"*20

	db = Mongo()

	# find who this user likes / dislikes already
	user = db.find_user(self.fbid)
	arr = (user.get("likes") or []) + (user.get("dislikes") or [])

	# find a random user
	res,i = db.find_random(),0
	while (res['usr'] in arr and i < 100):
		res,i = db.find_random(),i+1

	# no luck finding a random user
	if i == 100:
		raise NoProfiles

	# strip out the mongo id
	res.pop("_id", None)

	# create a profile object
	prof = Profile(res)
	try:
		prof.normalize()

		# and make a prediction!
		res['prediction'] = _predict(self,prof.gray)
		print 'predict:', res['prediction']
	except NoValidFaces, e:
		# no valid faces detected
		res['error'] = {
			'type': 'NoValidFaces',
			'message': e.message
		}
	except NoImageYet, e:
		# don't have both a liked_img and disliked_img yet
		res['error'] = {
			'type': 'NoImageYet',
			'message': e.message,
			'img_name': e.img_name
		}

	return res

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

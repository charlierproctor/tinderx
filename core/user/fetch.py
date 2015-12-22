from ..db import Mongo
from ..profile import Profile
from ..errors import NoValidFaces, NoImageYet, NoProfiles
import cv2
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
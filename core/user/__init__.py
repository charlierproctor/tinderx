import pickle

class User(object):
	def __init__(self,user):

		# the user's facebook id
		self.fbid = user.get('fbid')

		# arrays of the likes / dislikes
		self.likes = user.get('likes') or []
		self.dislikes = user.get('dislikes') or []

		# how many predictions have been correct so far.
		self.like_correct = user.get('like_correct')
		self.dislike_correct = user.get('dislike_correct')

		# prior liked / disliked averages
		self.liked_img = pickle.loads(user.get('liked_img')) if user.get('liked_img') else None
		self.disliked_img = pickle.loads(user.get('disliked_img')) if user.get('disliked_img') else None

	# import the various functions
	from swipe import swipe
	from fetch import fetch_profile,stats
	from auth import auth

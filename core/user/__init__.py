import pickle

class User(object):
	def __init__(self,user):

		# the user's facebook id
		self.fbid = user.get('fbid')

		# arrays of the likes / dislikes
		self.likes = user.get('likes')
		self.dislikes = user.get('dislikes')

		# prior liked / disliked averages
		self.liked_img = pickle.loads(user.get('liked_img'))
		self.disliked_img = pickle.loads(user.get('disliked_img'))

	from swipe import swipe,fetch_profile
	from auth import auth

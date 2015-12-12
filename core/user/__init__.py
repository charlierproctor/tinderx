class User(object):
	def __init__(self,fbid,likes,dislikes):
		self.fbid = fbid
		self.likes = likes
		self.dislikes = dislikes

	from swipe import swipe,fetch_profile
	from auth import auth

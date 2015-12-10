class User(object):
	def __init__(self,fbid):
		self.fbid = fbid

	from swipe import swipe,fetch_profile
	from auth import auth

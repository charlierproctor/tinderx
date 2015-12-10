class User(object):
	def __init__(self,fbid):
		self.fbid = fbid

	from swipe import swipe_left,swipe_right,next_profile
	from auth import auth

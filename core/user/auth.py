from ..db import Mongo
from facepy import GraphAPI

@classmethod
def auth(cls,fbid=None,fbAccessToken=None):

	# verify the params exist
	if (not fbid) or (not fbAccessToken):
		return False

	app_access_token = "1658892404386340|r90eMbKHygrFIlcJiPRmmKUkbY0"
	
	# query /debug_token to verify this user's access token
	graph = GraphAPI(app_access_token)
	res = graph.get('/debug_token', input_token=fbAccessToken)

	# verify the access token
	if res["data"] and res["data"]["is_valid"]:

		db = Mongo()

		# see if the user exists in MongoDB
		user = db.find_user(fbid)

		if not user:
			# if not, insert the user into the database
			user = db.insert_user({'fbid':fbid})

		return cls(fbid,user.get('likes'),user.get('dislikes'))
	else:
		return False

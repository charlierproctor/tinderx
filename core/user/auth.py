from ..db import Mongo
from facepy import GraphAPI

@classmethod
def auth(cls,user):
	app_access_token = "1658892404386340|r90eMbKHygrFIlcJiPRmmKUkbY0"
	
	# query /debug_token to verify this user's access token
	graph = GraphAPI(app_access_token)
	res = graph.get('/debug_token', input_token=user["fbAccessToken"])

	# verify the access token
	if res["data"] and res["data"]["is_valid"]:

		db = Mongo()

		# see if the user exists in MongoDB
		if not db.find_user(user["fbid"]):
			# if not, insert the user into the database
			db.insert_user(user)

		return cls(user["fbid"])
	else:
		return False

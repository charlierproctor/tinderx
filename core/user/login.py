from ..db import Mongo

@classmethod
def login(cls,user):
	db = Mongo()

	# see if the user exists	
	if not db.find_user(user["fbid"]):
		# if not, insert the user into the database
		db.insert_user(user)

	return cls(user["fbid"])
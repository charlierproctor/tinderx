from core.tinderx import TinderX
from core.user import User
from core.db import Mongo

from flask import Flask, request, jsonify

# configure the app
app = Flask(__name__, static_folder='dist',static_url_path='')

# send index.html on requests to /
@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/login', methods=['POST'])
def login():
	# grab / parse the request
	user = request.get_json()

	db = Mongo()

	# see if the user exists	
	if not db.find_user(user["fbid"]):
		# if not, insert the user into the database
		db.insert_user(user)

	return jsonify(success=True, fbid=user["fbid"])


# run the app
if __name__ == '__main__':
    app.run(debug=True)
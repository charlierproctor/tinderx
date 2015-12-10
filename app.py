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

# authorize a request
def _auth(req):
	return User.auth(fbid=req.cookies.get('fbid'),
		fbAccessToken=req.cookies.get('fbAccessToken'))

# log a user into the app
@app.route('/login', methods=['POST'])
def login(): 
	user = User.auth(**(request.get_json()))
	return jsonify(success=True, fbid=user.fbid) if user else (jsonify({'error': user}),403)

# allow a user to swipe left / right on a candidate
@app.route('/swipe', methods=['POST'])
def swipe():
	user = _auth(request)
	if user:
		# TODO: error handling here?
		user.swipe(**(request.get_json()))
		return jsonify(success=True)
	else:
		return jsonify({'error':user}),403

# fetch the next profile for this user
@app.route('/fetch')
def fetch():
	user = _auth(request)
	return jsonify(user.fetch_profile()) if user else (jsonify({'error': user}),403)

# run the app
if __name__ == '__main__':
    app.run(debug=True)
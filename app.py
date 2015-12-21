from core.user import User
from core.profile import Profile
from core.db import Mongo

from flask import Flask, request, jsonify, g, abort

# configure the app
app = Flask(__name__, static_folder='dist',static_url_path='')

# GET /: send the angular app (index.html) to the client
@app.route('/')
def root(): 
	# send index.html
	return app.send_static_file('index.html')

# authorize a request
@app.before_request
def before():
	# authorize a user based on the fbid, fbAcessToken stored in the cookies
	g.user = User.auth(fbid=request.cookies.get('fbid'),
		fbAccessToken=request.cookies.get('fbAccessToken'))

# 403 error handler
@app.errorhandler(403)
def access_denied(e):
	# jsonify the message
    return jsonify(message="403 Forbidden"), 403

# 404 error handler
@app.errorhandler(404)
def not_found(e):
	# jsonify the message
    return jsonify(message="404 Not Found"), 404

# POST /login: log a user into the app
@app.route('/login', methods=['POST'])
def login(**kwargs): 
	# authorize a user based on the request body (if the user isn't already logged in)
	user = User.auth(**(request.get_json())) if not g.user else g.user
	return jsonify(fbid=user.fbid,**kwargs) if user else abort(403)

# GET /fetch: fetch a single user profile
@app.route('/fetch')
def fetch(**kwargs):
	# call user.fetch_profile()
	return jsonify(next=g.user.fetch_profile(),**kwargs) if g.user else abort(403)

# POST /swipe: allow a user to swipe left / right on a candidate
@app.route('/swipe', methods=['POST'])
def swipe(**kwargs):
	# call user.swipe() with the request body. call fetch to return the next candidate
	return fetch(status=g.user.swipe(**(request.get_json())),**kwargs) if g.user else abort(403)
		

# run the app
if __name__ == '__main__':
    app.run(debug=True)
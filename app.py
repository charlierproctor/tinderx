from core.tinderx import TinderX
from core.user import User
from core.db import Mongo

from flask import Flask, request, jsonify, g, abort

# configure the app
app = Flask(__name__, static_folder='dist',static_url_path='')

# send index.html on requests to /
@app.route('/')
def root(): 
	return app.send_static_file('index.html')

# authorize a request
@app.before_request
def before():
	g.user = User.auth(fbid=request.cookies.get('fbid'),
		fbAccessToken=request.cookies.get('fbAccessToken'))

# log a user into the app
@app.route('/login', methods=['POST'])
def login(**kwargs): 
	user = User.auth(**(request.get_json())) if not g.user else g.user
	return jsonify(fbid=user.fbid,**kwargs) if user else abort(403)

# fetch the next profile for this user
@app.route('/fetch')
def fetch(**kwargs):
	return jsonify(next=g.user.fetch_profile(),**kwargs) if g.user else abort(403)

# allow a user to swipe left / right on a candidate
@app.route('/swipe', methods=['POST'])
def swipe(**kwargs):
	return fetch(status=g.user.swipe(**(request.get_json())),**kwargs) if g.user else abort(403)
		

# run the app
if __name__ == '__main__':
    app.run(debug=True)
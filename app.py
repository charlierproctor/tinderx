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
	return User.auth(req.get_json())

# log a user into the app
@app.route('/login', methods=['POST'])
def login(): 
	return jsonify(success=True, fbid=_auth(request).fbid)


# run the app
if __name__ == '__main__':
    app.run(debug=True)
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
	# grab the request and log the user in
	user = User.login(request.get_json())

	return jsonify(success=True, fbid=user.fbid)


# run the app
if __name__ == '__main__':
    app.run(debug=True)
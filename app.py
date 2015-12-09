from core.tinderx import TinderX
from core.user import User
from core.db import Mongo

from flask import Flask

# configure the app
app = Flask(__name__, static_folder='dist',static_url_path='')

# send index.html on requests to /
@app.route('/')
def root():
    return app.send_static_file('index.html')

# run the app
if __name__ == '__main__':
    app.run()
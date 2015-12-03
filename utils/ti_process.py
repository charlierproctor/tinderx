import urllib, cv2, sys, os
import numpy as np
from pymongo import MongoClient

# check usage
if len(sys.argv) < 2:
	sys.stderr.write("USAGE: python ti_process.py NUM_PROFILES\n")
	sys.exit(os.EX_USAGE)

# connect to the database
client = MongoClient()
db = client.tinderx
profiles_collection = db.tinder_profiles

# query the database
profiles = profiles_collection.find({}).limit(int(sys.argv[1]))

# iterate through the profiles
for profile in profiles:

	# download the image
	req = urllib.urlopen("http://images.gotinder.com" + profile['img'])

	# convert to cv2 image
	arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
	img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

	# show the image (for one second)
	cv2.imshow(profile['name'].encode('ascii', 'ignore'),img)
	cv2.waitKey(1000)

cv2.destroyAllWindows()
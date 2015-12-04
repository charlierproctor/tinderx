import urllib, cv2, sys, os
import numpy as np
from pymongo import MongoClient

# check usage
if len(sys.argv) < 2:
	sys.stderr.write("USAGE: python ti_process.py NUM_PROFILES\n")
	sys.exit(os.EX_USAGE)

HAAR_EYES = "../lib/opencv3/haarcascades/haarcascade_eye.xml"
HAAR_FACES = "../lib/opencv3/haarcascades/haarcascade_frontalface_default.xml"

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

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# detect and draw faces
	faceCascade = cv2.CascadeClassifier(HAAR_FACES)

	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(50, 50)
	)

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

	# detect and draw eyes
	eyeCascade = cv2.CascadeClassifier(HAAR_EYES)

	eyes = eyeCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(10, 10)
	)

	for (x, y, w, h) in eyes:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

	# show the image (for 1/2 second)
	cv2.imshow(profile['name'].encode('ascii', 'ignore'),img)
	cv2.waitKey(500)
	cv2.destroyAllWindows()
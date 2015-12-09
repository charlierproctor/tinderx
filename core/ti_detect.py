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

# show the image (for 1/2 second)
def show_img(name,img):
	cv2.imshow(name.encode('ascii', 'ignore'),img)
	cv2.waitKey(500)
	cv2.destroyAllWindows()

# iterate through the profiles
for profile in profiles:

	# download the image
	req = urllib.urlopen("http://images.gotinder.com" + profile['img'])

	# convert to cv2 image
	arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
	img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

	# convert to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# detect faces
	faces = cv2.CascadeClassifier(HAAR_FACES).detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(50, 50)
	)

	# draw the faces on the image
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

	# detect eyes
	eyes = cv2.CascadeClassifier(HAAR_EYES).detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(10, 10)
	)

	# draw the eyes on the image
	for (x, y, w, h) in eyes:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

	show_img(profile['name'],img)

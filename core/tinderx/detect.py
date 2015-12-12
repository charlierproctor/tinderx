import urllib, cv2, sys, os
import numpy as np
from .. import db

HAAR_EYES = os.path.dirname(__file__) + "/../../lib/opencv3/haarcascades/haarcascade_eye.xml"
HAAR_FACES = os.path.dirname(__file__) + "/../../lib/opencv3/haarcascades/haarcascade_frontalface_default.xml"

# show the image (for 1/2 second)
def _show_img(img,name="tinderx",time=500):
	cv2.imshow(name.encode('ascii', 'ignore'),img)
	cv2.waitKey(time)
	cv2.destroyAllWindows()

# download the image from http://images.gotinder.com/[img_url]
def _download_img(url):
	# send the http request
	req = urllib.urlopen("http://images.gotinder.com" + url)

	# convert to cv2 image
	arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
	return cv2.imdecode(arr, cv2.IMREAD_COLOR)

# detect the faces in an image
def _detect_faces(img,draw=False):
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
	if draw:
		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

	return faces

# detect the eyes in an image
def _detect_eyes(img,draw=False):
	# convert to grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# detect eyes
	eyes = cv2.CascadeClassifier(HAAR_EYES).detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(10, 10)
	)

	# draw the eyes on the image
	if draw:
		for (x, y, w, h) in eyes:
			cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

	return eyes
	
def normalize(self):
	# download the image
	img = _download_img(self.user.img)

	# detect the faces
	faces = _detect_faces(img)

# when this file is executed directly
if __name__ == '__main__':

	# load the profiles from mongodb
	profiles = db.Mongo().load_profiles(int(sys.argv[1]))

	# iterate through the profiles
	for profile in profiles:

		# downloading the image
		img = _download_img(profile['img'])
		
		# detecting faces, eyes
		faces = _detect_faces(img,draw=True)
		eyes = _detect_eyes(img,draw=True)

		# and display the image
		_show_img(img,profile['name'])

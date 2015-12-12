import cv2, os
import numpy as np

HAAR_EYES = os.path.dirname(__file__) + "/../../lib/opencv3/haarcascades/haarcascade_eye.xml"
HAAR_FACES = os.path.dirname(__file__) + "/../../lib/opencv3/haarcascades/haarcascade_frontalface_default.xml"

# detect the faces in an image
def detect_faces(self,draw=False):

	# detect faces
	self.faces = cv2.CascadeClassifier(HAAR_FACES).detectMultiScale(
		self.gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(50, 50)
	)

	# draw the faces on the image
	if draw:
		for (x, y, w, h) in self.faces:
			cv2.rectangle(self.img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# detect the eyes in an image
def detect_eyes(self,draw=False):

	# detect eyes
	self.eyes = cv2.CascadeClassifier(HAAR_EYES).detectMultiScale(
		self.gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(10, 10)
	)

	# draw the eyes on the image
	if draw:
		for (x, y, w, h) in self.eyes:
			cv2.rectangle(self.img, (x, y), (x+w, y+h), (255, 0, 0), 2)
	
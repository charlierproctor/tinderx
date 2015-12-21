import cv2, os
import numpy as np
from ..errors import NoValidFaces

HAAR_EYES = os.path.dirname(__file__) + "/../../lib/opencv3/haarcascades/haarcascade_eye.xml"
HAAR_FACES = os.path.dirname(__file__) + "/../../lib/opencv3/haarcascades/haarcascade_frontalface_default.xml"

# detect the faces in an image
def detect_faces(self,draw=False):

	# detect faces
	self.faces = cv2.CascadeClassifier(HAAR_FACES).detectMultiScale(
		self.gray,
		scaleFactor=1.1,
		minNeighbors=3,
		minSize=(25, 25)
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
		minNeighbors=3,
		minSize=(5, 5)
	)

	# draw the eyes on the image
	if draw:
		for (x, y, w, h) in self.eyes:
			cv2.rectangle(self.img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# calculate the center of each eye
def calculate_pupils(self,draw=False):

	# a pupil is the center of the eye
	for (x, y, w, h) in self.eyes:
		self.pupils.append((x + w/2, y + h/2))

	# draw the pupils on the img
	if draw:
		for (x,y) in self.pupils:
			cv2.circle(self.img, (x,y), 5, (255, 0, 0), 2)

# determine if a point lies in a rectangle
# pt specified as (x,y)
# rect specified as (x,y,w,h)
def _point_in_rect(pt,rect):
	return ((pt[0] >= rect[0]) 
	and (pt[0] <= rect[0] + rect[2]) 
	and (pt[1] >= rect[1])
	and (pt[1] <= rect[1] + rect[3]))

# a valid face is a face with at least ONE eye.
def _valid_faces(self):

	valids = []
	for face in self.faces:
		eyes = 0

		# determine how many eyes this face has
		for eye in self.pupils:
			if _point_in_rect(eye,face):
				eyes += 1

		# if the face has at least one eye, keep it
		if eyes >= 1:
			valids.append(face)

	return valids


# the best face is the largest valid face
def best_face(self):
	valids = _valid_faces(self)

	self.best = max(valids,key=lambda face: (face[2]**2 + face[3]**2)**0.5) if len(valids) > 0 else None
	print "Best: ", self.best

	if not isinstance(self.best,np.ndarray):
		raise NoValidFaces
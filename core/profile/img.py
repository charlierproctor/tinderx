import urllib, cv2
import numpy as np
import pdb

# create a grayscale representation of this image
def create_gray(self):
	self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

# download the image from http://images.gotinder.com/[img_url]
def download_img(self):
	# send the http request
	req = urllib.urlopen("http://images.gotinder.com" + self.img_url)

	# convert to cv2 image
	arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
	self.img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

# crop the image (and the grayscale)
def _crop(self,x,y,w,h):
	self.img = self.img[x:x+w,y:y+h]
	self.gray = self.gray[x:x+w,y:y+h]

IMG_SIZE = (100,100)

# resize the image (and the grayscale)
def _resize(self,w,h):
	self.gray = cv2.resize(self.gray,(w,h))
	self.img = cv2.resize(self.img,(w,h))

def normalize(self):

	# download image, create the grayscale
	self.download_img()
	self.create_gray()

	# detect the faces
	self.detect_faces()

	# detect eyes, calculate pupils
	self.detect_eyes()
	self.calculate_pupils()

	# determine the best face
	self.best_face()

	# crop the image down to just this face. then resize it to IMG_SIZE
	_crop(self,*(self.best))
	_resize(self,*IMG_SIZE)




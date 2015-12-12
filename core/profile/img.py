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
def crop(self,x,y,w,h):
	self.img = self.img[x:x+w,y:y+h]
	self.gray = self.gray[x:x+w,y:y+h] if self.gray else None

def normalize(self):

	# download image, create the grayscale
	self.download_img()
	self.create_gray()

	# detect the faces
	self.detect_faces()
	self.detect_eyes()

	self.calculate_pupils()
	pdb.set_trace()



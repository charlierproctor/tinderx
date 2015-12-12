import urllib, cv2
import numpy as np

# download the image from http://images.gotinder.com/[img_url]
def download_img(self):
	# send the http request
	req = urllib.urlopen("http://images.gotinder.com" + self.img_url)

	# convert to cv2 image
	arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
	self.img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
from . import Profile
from .. import db
import sys,cv2

# show the image (for 1/2 second)
def _show_img(img,name="tinderx",time=500):
	cv2.imshow(name.encode('ascii', 'ignore'),img)
	cv2.waitKey(time)
	cv2.destroyAllWindows()

# when this file is executed directly
if __name__ == '__main__':

	# load the profiles from mongodb
	profiles = db.Mongo().load_profiles(int(sys.argv[1]))

	# iterate through the profiles
	for profile in profiles:

		# create the profile and download the image
		prof = Profile(profile)
		prof.download_img()
		prof.create_gray()
		
		# detecting faces, eyes
		prof.detect_faces(draw=True)
		prof.detect_eyes(draw=True)

		# and display the image
		_show_img(prof.img,prof.name)

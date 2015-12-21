from core.db import Mongo
from core.user import User
import sys,os,cv2

# show the image (for 1/2 second)
def _show_img(img,name="tinderx",time=10000):
	cv2.imshow(name.encode('ascii', 'ignore'),img)
	cv2.waitKey(time)
	cv2.destroyAllWindows()

if __name__ == '__main__':

	# check usage	
	if len(sys.argv) != 3:
		sys.stderr.write("USAGE: python -m utils.show fbid img_name\n")
		sys.exit(os.EX_USAGE)

	db = Mongo()

	# find this user
	user = User(db.find_user(sys.argv[1]))

	# and show the image
	if sys.argv[2] == 'liked_img':
		_show_img(user.liked_img,name=sys.argv[2])
	else:
		_show_img(user.disliked_img,name=sys.argv[2])


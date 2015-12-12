class Profile(object):
	def __init__(self,profile):

		# username / name / age
		self.username = profile.get('usr')
		self.name = profile.get('name')
		self.age = profile.get('age')

		# the user's image url and the teaser
		self.img_url = profile.get('img')
		self.teaser = profile.get('tsr')

		# the user's image (needs to be downloaded)
		self.img = None

	from img import download_img
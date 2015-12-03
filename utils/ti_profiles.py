from lxml import html
from pymongo import MongoClient
import string,requests,itertools,sys,os

# check usage
if len(sys.argv) < 2:
	sys.stderr.write("USAGE: python ti_profiles.py USERNAME_LENGTH\n")
	sys.exit(os.EX_USAGE)

TINDER_ROOT = 'https://www.gotinder.com/@'

# xpaths
NAME_XPATH = '//*[@id="name"]/text()'
IMG_XPATH = '//*[@id="user-photo"]/@src'
AGE_XPATH = '//*[@id="age"]/text()'
TEASER_XPATH = '//*[@id="teaser"]/text()'

# download / parse the results for this username from TINDER_ROOT/@[username]
def process(username):

	# make and tree'ify the request
	page = requests.get(TINDER_ROOT + username)
	tree = html.fromstring(page.content)

	# results dictionary
	results = {
		"usr": username
	}

	# parse the img... must have this or the user doesn't exist.
	xp_img = tree.xpath(IMG_XPATH)
	if (len(xp_img)) == 1:
		results["img"] = xp_img[0].replace("http://images.gotinder.com", "", 1)
	else:
		return False

	# parse the name
	xp_name = tree.xpath(NAME_XPATH)
	if (len(xp_name) == 1):
		results["name"] = xp_name[0][:-1]

	# parse the age
	xp_age = tree.xpath(AGE_XPATH)
	if (len(xp_age) == 1):
		results["age"] = int(xp_age[0])

	# parse the teaser
	xp_teaser = tree.xpath(TEASER_XPATH)
	if (len(xp_teaser) == 1):
		results["tsr"] = xp_teaser[0]

	return results

# connect to the database
client = MongoClient()
db = client.tinderx
profiles_collection = db.tinder_profiles

POSSIBLE_LETTERS = '_' + string.digits + string.uppercase

# generate all possible usernames of the given length (or less)
for i in xrange(int(sys.argv[1])):
	for username in itertools.imap(''.join, itertools.product(POSSIBLE_LETTERS, repeat=i)):

		# process this username
		results = process(username)

		# save / print the results
		if results:
			profiles_collection.insert_one(results)
			print username, results


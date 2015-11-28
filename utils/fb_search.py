import os,sys,requests

FB_URL = "https://graph.facebook.com/v2.5"

ACCESS_TOKEN = os.environ["FB_ACCESS_TOKEN"]

r = requests.get(FB_URL + "/search", params = {
	'access_token': ACCESS_TOKEN,
	'type': sys.argv[1],
	'q': sys.argv[2]
})

print r.text
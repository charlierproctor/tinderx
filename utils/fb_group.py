import os,sys,requests,uuid,json

FB_URL = "https://graph.facebook.com/v2.5"

ACCESS_TOKEN = os.environ["FB_ACCESS_TOKEN"]

FILE_PATH = "../data/"

CHUNK_SIZE = 512

group_url = FB_URL + "/" + sys.argv[1]

group_request = requests.get(group_url, params = {
	'access_token': ACCESS_TOKEN,
	'fields': 'id,name'
})

group_info = group_request.json()
FILE_PATH += group_info["id"] + "/"

if os.path.exists(FILE_PATH):
	sys.stderr.write("directory exists\n")
	sys.exit()
else:
	os.makedirs(FILE_PATH)

members_request = requests.get(group_url + "/members", params = {
	'access_token': ACCESS_TOKEN,
	'limit': '1000'
})

members = members_request.json()["data"]

saved_users = []

for user in members:

	img = requests.get(FB_URL + "/" + user["id"] + "/picture", params = {
		'access_token': ACCESS_TOKEN,
		'type': 'large'
	})

	filename = str(uuid.uuid4()) + ".jpg"

	with open(FILE_PATH + filename, 'wb') as fd:
		for chunk in img.iter_content(CHUNK_SIZE):
			fd.write(chunk)

	save_me = {
		"name": user.get("name"),
		"id": user["id"],
		"photo": filename
	}

	saved_users.append(save_me)
	
	sys.stdout.write(".")
	sys.stdout.flush()

final = {
	"group": group_info,
	"users": saved_users
}

with open(FILE_PATH + "group.json", "w") as f:
	json.dump(final,f)
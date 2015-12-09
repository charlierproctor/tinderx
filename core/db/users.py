# load users collection from mongodb
def _collection(self):
	return self.db.users
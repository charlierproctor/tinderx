# generic application error. superclass for other errors.
class AppError(Exception):
	
	def __init__(self,status,message):
		self.status = status
		self.message = message

	def __str__(self):
		return repr(self.message)

# failed to detect any valid faces
class NoValidFaces(AppError):
	def __init__(self):
		AppError.__init__(self,500,"No valid faces detected.")
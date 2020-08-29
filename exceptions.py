

class MyErrors(Exception):
	def __init__(self, error):
	
		super().__init__(error)

		self.error = error

class OutOfQuestions(MyErrors):
	pass
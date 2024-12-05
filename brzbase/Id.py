import uuid

from . import Yeast

class Id:

	server_id = None
	
	brzbase = None

	def __init__(self, brzbase):
		self.brzbase = brzbase
		if not self.server_id:
			# print("a __init__: serverid:", self.server_id)
			self.server_id = self.new_id()
			# print("b __init__: serverid:", self.server_id)

		print("__init__: serverid:", self.server_id)

	def new_id(self):
		return Yeast.encode(uuid.uuid1().int)

	def set_server_id(self, id):
		self.server_id = id

	def get_server_id(self):
		return self.server_id

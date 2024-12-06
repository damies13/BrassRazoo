import uuid

from . import Yeast

class Id:

	brzbase = None

	def __init__(self, brzbase):
		self.brzbase = brzbase

	def new_id(self):
		return Yeast.encode(uuid.uuid1().int)

	# def set_server_id(self, id):
	# 	self.server_id = id
	#
	# def get_server_id(self):
	# 	return self.server_id

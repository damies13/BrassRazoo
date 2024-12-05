
# import uuid
# from . import Yeast
# from . import Id

class Record:

	records = {}

	brzbase = None

	def __init__(self, brzbase):
		self.brzbase = brzbase

	def new_record(self, creator):

		# myid = str(uuid.uuid1())
		# myid = Yeast.encode(uuid.uuid1().int)
		myid = self.brzbase.Id.new_id()

		record = {
			"Record ID": myid,
			"Revision": 0,
			"Type": "",
			"Status": "",
			"Creator": creator,
			"Description": "",
			"Signature": "",
		}

		return record

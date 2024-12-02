
import uuid

from . import Yeast

class Record:

	records = {}

	def __init__(self):
		pass

	def new_record(self, creator):

		# myid = str(uuid.uuid1())
		myid = Yeast.encode(uuid.uuid1().int)

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

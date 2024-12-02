
import uuid


class Record:

	records = {}

	def __init__(self):
		pass

	def new_record(self, creator):

		myid = str(uuid.uuid1())

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

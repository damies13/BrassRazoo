import hashlib
import json
import uuid

class Block:

	blocks = {}

	def __init__(self):
		pass

	def new_block(self, previous_id, transactions):
		myid = str(uuid.uuid1())
		self.blocks[myid] = {}
		self.blocks[myid]["Id"] = myid
		self.blocks[myid]["Previous Id"] = previous_id
		self.blocks[myid]["Transactions"] = transactions

		print(self.blocks[myid])

		self.blocks[myid]["Hash"] = hashlib.sha256(json.dumps(self.blocks[myid]).encode("utf-8")).hexdigest()

		print(self.blocks[myid])

		print(self.blocks)

		return myid

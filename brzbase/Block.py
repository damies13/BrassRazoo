import hashlib
import json
import uuid

class Block:

	blocks = {}

	def __init__(self):
		self.genisis_block()

	def genisis_block(self):

		genisis = "Brass Razoo Genisis Block"


		# myid = "d69f7446-ac9f-11ef-b3cd-1062e51b6a98"
		myid = "00000000-0000-1000-0000-000000000000"
		# myid = str(uuid.uuid1())
		# myid = str(uuid.uuid1(node=genisis))
		# myid = str(uuid.uuid1(node=genisis, clock_seq=88888))
		# myid = str(uuid.uuid1(node=genisis, clock_seq="88888888888888"))
		self.blocks[myid] = {}

		transactions = {}

		self.blocks[myid]["Id"] = myid
		self.blocks[myid]["Previous Id"] = genisis
		self.blocks[myid]["Previous Hash"] = genisis
		self.blocks[myid]["Transactions"] = transactions

		print(self.blocks[myid])

		self.blocks[myid]["Hash"] = hashlib.sha256(json.dumps(self.blocks[myid]).encode("utf-8")).hexdigest()

		print(self.blocks[myid])

		print(self.blocks)


	def new_block(self, previous_id, transactions):
		myid = str(uuid.uuid1())
		self.blocks[myid] = {}
		self.blocks[myid]["Id"] = myid
		self.blocks[myid]["Previous Id"] = previous_id
		self.blocks[myid]["Previous Hash"] = self.blocks[previous_id]["Hash"]
		self.blocks[myid]["Transactions"] = transactions

		print(self.blocks[myid])

		self.blocks[myid]["Hash"] = hashlib.sha256(json.dumps(self.blocks[myid]).encode("utf-8")).hexdigest()

		print(self.blocks[myid])

		print(self.blocks)

		return myid

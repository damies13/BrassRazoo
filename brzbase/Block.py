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

		records = {}

		records["8d98d089-2f4a-469b-85a8-f4e59fd2cc4c"] = {
															"Record ID": "8d98d089-2f4a-469b-85a8-f4e59fd2cc4c",
															"Revision": 0,
															"Type": "Account",
															"Status": "Completed",
															"Creator": "8d98d089-2f4a-469b-85a8-f4e59fd2cc4c",
															"Description": "Brass Razoo Foundation",
															"Signature": "",
															"IsValid": True
														}
		records["546c426f-3562-48de-a60e-5669ff501ccb"] = {
															"Record ID": "546c426f-3562-48de-a60e-5669ff501ccb",
															"Revision": 0,
															"Type": "Transfer",
															"Status": "Completed",
															"Creator": "8d98d089-2f4a-469b-85a8-f4e59fd2cc4c",
															"Description": "Initial Ballance",
															"Signature": "",
															"Recipient": "8d98d089-2f4a-469b-85a8-f4e59fd2cc4c",
															"Ammount": 999999999999999.999,
															"IsValid": True
														}
		records["63275786-1bf2-4745-975b-065646395a3c"] = {
															"Record ID": "63275786-1bf2-4745-975b-065646395a3c",
															"Revision": 0,
															"Type": "Server",
															"Status": "Completed",
															"Creator": "63275786-1bf2-4745-975b-065646395a3c",
															"Description": "brzserver_v0.0.1",
															"Signature": "",
															"IP6": "",
															"IsValid": True
														}
		records["a63e853f-a7ac-4f5e-b63e-a52f93019d06"] = {
															"Record ID": "a63e853f-a7ac-4f5e-b63e-a52f93019d06",
															"Revision": 0,
															"Type": "Stake",
															"Status": "Completed",
															"Creator": "8d98d089-2f4a-469b-85a8-f4e59fd2cc4c",
															"Description": "Initial Stake",
															"Server": "63275786-1bf2-4745-975b-065646395a3c",
															"Ammount": 888.000,
															"Signature": "",
															"IsValid": True
														}
		# records["db1c309e-86c2-4348-9b01-a96940961b95"]
		# records["2190090c-3ddc-4ac5-b12e-49dedd628ab2"]
		# records["df48c0a2-0ae1-4772-857a-c79b4cc6cc26"]
		# records["ce47907f-8972-44e4-8004-04422934776f"]
		# records["cc64e2e1-6f1f-4a97-bab2-a02d1a86c367"]
		# records["b1993603-2377-477a-afe3-31864349ddc1"]
		# records["b06949cb-d5bd-4682-b67b-c472520b7839"]
		# records["ca6e383a-fd8f-4c16-a03e-3e6a451b7cec"]
		# records["a5065979-9750-4fbe-a341-a27c20379220"]
		# records["b07d523a-1976-4f0b-8e26-472c82ad34b3"]
		# records["ecfe0b3b-75da-46e7-8bdf-ca286fa5de9f"]
		# records["04cba67e-7af1-4535-b5ff-e08d95af7484"]
		# records["25cd7974-0e38-4310-915c-1dfa0bdfcf29"]
		# records["57f94d40-1b48-4516-9099-0aa89350e35f"]
		# records["2d361a41-9ffb-47db-b79e-d8a30c654edd"]
		# records["7386bb61-7356-4428-8c7c-922292975def"]
		# records["590fa542-8856-4f47-8902-d0ea05765f14"]
		# records["b92e1ca4-dac7-4a8c-8a1c-0bf7e7bd5417"]
		# records["e63a223f-2eca-4754-ad9a-cf53b4a2aca8"]
		# records["53d48e39-281f-46c5-8d60-409a3d39666f"]
		# records["d9514e63-6a30-481a-8d86-48e81b160b7f"]
		# records["8de62e68-c04f-4845-9973-66b6a16dc027"]
		# records["ac98a270-7e1f-4f3e-86a7-35e4073b1d5a"]
		# records["7f60a9a9-ae36-4b52-bd04-bc9ebceb2e04"]
		# records["486ead0d-6bb9-4389-af92-bdc7b0c2b2a1"]
		# records["57937502-c8db-4acf-ab66-9bff345b3efc"]
		# records["7aae3565-0755-4ceb-875c-f835af133fde"]
		# records["4e09f500-b02d-49b1-8ddd-389fde9897a3"]
		# records["4ef53a9d-7e6a-40af-9857-48c21584db2b"]
		# records["41528bc7-774f-46f2-b8fa-38020f81fab8"]
		# records["fe394656-eb27-4491-a4f5-31e219327e8f"]
		# records["ed5406f5-4d54-4a15-b8de-e14ce73cc5e5"]
		# records["8116fdb5-4ad1-496a-b001-36cbcc21d8d7"]
		# records["e952cba5-2813-49c9-8e1b-0a38ab5b09f1"]
		# records["883e7f7d-63c5-4b72-98f0-376beeb000ec"]
		# records["b353aa36-fb99-4453-83f7-ffdb7873ac6f"]
		# records["a57954df-ceb5-4d3a-8dfe-350b932b704e"]
		# records["bf290f56-0753-4497-b757-65b68e3c69b7"]
		# records["296dcae5-f84b-489f-83db-c30e5b5a05c0"]
		# records["f14e3d78-d1b6-423b-b17d-465909b93b7e"]
		# records["14dfbbe6-b7ec-4b31-b417-423c094071e5"]
		# records["1f0f8164-8ce2-497f-abb1-d0a1321883ab"]
		# records["2df3b53d-5741-4922-8666-e073fdb4dc22"]
		# records["67fe35a6-8975-410a-978a-634b05dfb9c8"]
		# records["7021bf7b-5b99-43d8-8efe-a4651a5b32b4"]
		# records["e45eb0c5-b0fa-4f48-93ff-27228f9f40f9"]


		self.blocks[myid]["Id"] = myid
		self.blocks[myid]["Previous Id"] = genisis
		self.blocks[myid]["Previous Hash"] = genisis
		self.blocks[myid]["Records"] = records

		# print(self.blocks[myid])

		self.blocks[myid]["Hash"] = hashlib.sha256(json.dumps(self.blocks[myid]).encode("utf-8")).hexdigest()

		# print(self.blocks[myid])

		# print(self.blocks)

	def get_block(self, block_id):
		try:
			return self.blocks[block_id]
		except:
			raise Exception("No block found with Id", block_id) 

	def new_block(self, previous_id, transactions):
		myid = str(uuid.uuid1())
		self.blocks[myid] = {}
		self.blocks[myid]["Id"] = myid
		self.blocks[myid]["Previous Id"] = previous_id
		self.blocks[myid]["Previous Hash"] = self.blocks[previous_id]["Hash"]
		self.blocks[myid]["Transactions"] = transactions

		# print(self.blocks[myid])

		self.blocks[myid]["Hash"] = hashlib.sha256(json.dumps(self.blocks[myid]).encode("utf-8")).hexdigest()

		# print(self.blocks[myid])

		# print(self.blocks)

		return myid

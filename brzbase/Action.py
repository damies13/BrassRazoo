
from . import Record

class Action:

	def __init__(self):
		pass


class Rule:

	def new_rule(self, creator):
		record = Record.Record().new_record(creator)
		record["Type"] = "Action"
		record["SubType"] = "Rule"
		record["Data"] = ""

		return record

class Task:

	def new_task(self, creator):
		record = Record.Record().new_record(creator)
		record["Type"] = "Action"
		record["SubType"] = "Task"
		record["Data"] = ""

		return record

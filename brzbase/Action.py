
# from . import Record

class Action:

	brzbase = None

	def __init__(self, brzbase):
		self.brzbase = brzbase


class Rule:

	brzbase = None

	def __init__(self, brzbase):
		self.brzbase = brzbase

	def new_rule(self, creator):
		record = self.brzbase.Record.new_record(creator)
		record["Type"] = "Action"
		record["SubType"] = "Rule"
		record["Data"] = ""

		return record


class Task:

	brzbase = None

	def __init__(self, brzbase):
		self.brzbase = brzbase

	def new_task(self, creator):
		record = self.brzbase.Record.new_record(creator)
		record["Type"] = "Action"
		record["SubType"] = "Task"
		record["Data"] = ""

		return record

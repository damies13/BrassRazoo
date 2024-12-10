
from . import Block
from . import Record
from . import Action
from . import Yeast
from . import Id
from . import Shard
from . import Security

class brzbase:

	Block = None
	Record = None
	Action = None
	Rule = None
	Task = None
	Yeast = Yeast
	Id = None
	Shard = None

	def __init__(self):
		self.Block = Block.Block(self)
		self.Record = Record.Record(self)
		self.Action = Action.Action(self)
		self.Rule = Action.Rule(self)
		self.Task = Action.Task(self)
		# self.Yeast = Yeast
		self.Id = Id.Id(self)
		self.Shard = Shard.Shard(self)


# from . import Id

class Shard:

	shard_size = 1

	brzbase = None

	def __init__(self, brzbase):
		self.brzbase = brzbase

	def get_shard_size(self):
		return self.shard_size

	def set_shard_size(self, size):
		self.shard_size = size

	def get_current_shard(self):
		shard = None
		if self.shard_size > 0:
			serverid = self.brzbase.Id.get_server_id()
			shard = serverid[-self.shard_size]
		return shard

	def get_next_shard(self):
		serverid = self.brzbase.Id.get_server_id()
		shard = serverid[-(self.shard_size+1)]
		return shard

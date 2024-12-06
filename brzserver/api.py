
import bottle

app = bottle.Bottle()

class api(bottle.Bottle):

	brzserver = None

	def __init__(self, brzserver_value):
		self.app = app
		self.brzserver = brzserver_value
		self.app.brzserver = brzserver_value
		# brzserver = brzserver_value

	@app.route("/api/server")
	def server_details():
		data = {}
		data["server_id"] = app.brzserver.brzbase.Id.get_server_id()
		# data["server_id"] = brzserver.brzbase.Id.get_server_id()
		return data

	@app.route("/api/block/<blockid>")
	def server_details(blockid="BrassRazooGenisisBlock"):
		try:
			data = app.brzserver.brzbase.Block.get_block(blockid)
		except:
			bottle.abort(404, f"No block found with id: {blockid}")
		return data

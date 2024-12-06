
import sys
import os

import api
import webui
import bottle

dir_path = os.path.dirname(os.path.realpath(__file__))
base_path = os.path.abspath(os.path.join(dir_path, ".."))
sys.path.insert(0, base_path)
import brzbase


class brzserver:

	app_name = "Brass Razoo"
	app_version = "2024.12.6.1651"

	api = None
	webui = None
	brzbase = brzbase.brzbase()

	def __init__(self):
		# server start
		self.api = api.api(self)
		self.webui = webui.webui(self)

		self.app = bottle.Bottle()

		# self.app.mount('/api/', self.api.app)
		# self.app.mount('/webui/', self.webui.app)
		self.app.merge(self.api.app)
		self.app.merge(self.webui.app)

		self.app.run(host='localhost', port=8080, debug=True)




if __name__ == '__main__':
	brzserver()

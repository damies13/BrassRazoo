
import sys
import os
import yaml

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

	config = {}
	config_file = "config.yaml"

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


		self.config = self.load_config(self.config_file)

		if "server_id" not in self.config:
			self.config["server_id"] = self.brzbase.Id.new_id()
		print("serverid:", self.config["server_id"])


		self.app.run(host='localhost', port=8080, debug=True)

		self.on_closing()

	def on_closing(self):
		self.save_config(self.config_file, self.config)

	def load_config(self, configfile):
		config = {}
		if os.path.exists(configfile):
			with open(configfile, 'r') as file:
				config = yaml.safe_load(file)
		return config

	def save_config(self, configfile, configdata):
		with open(configfile, 'w') as file:
			yaml.dump(configdata, file)
		return 0

if __name__ == '__main__':
	brzserver()

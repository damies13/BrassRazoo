
import bottle

app = bottle.Bottle()

class webui(bottle.Bottle):

	brzserver = None

	def __init__(self, brzserver):
		self.app = app
		self.brzserver = brzserver
		self.app.brzserver = brzserver

	@app.route("/")
	def redirect_to_webui():
		bottle.redirect('/ui/index.html', code=None)

	@app.route("/ui/index.html")
	def webui_home():
		return f"""
		<html>
			<head>
				<title>{app.brzserver.app_name} {app.brzserver.app_version}</title>
			</head>
			<body>
				<div id="msg-welcome">
					<h1>Welcome to {app.brzserver.app_name}</h1>
				</div>
				<div id="msg-server-details">
				</div>
			</body>
		</html>
		"""

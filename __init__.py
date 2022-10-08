from pypresence import Presence
import time
from binaryninja import *
from binaryninjaui import DockHandler

class DiscordNinja(binaryninja.BackgroundTaskThread):
	DISCORD_CLIENTID = "1024650070848716902"
	
	def __init__(self):
		BackgroundTaskThread.__init__(self, can_cancel = False)
		self.discord = Presence(self.DISCORD_CLIENTID)
		self.discord.connect()
		self.running = True

	def run(self):
		dockhandler = DockHandler.getActiveDockHandler()

		while self.running:
			state = "Slacking off..."

			if dockhandler.getViewFrame():
				state = f"{dockhandler.getViewFrame().getShortFileName()}"

			self.discord.update(
				details = state if state == "Slacking off..." else "📁 " + state,
				large_image = "big_logo",
				large_text = "Binary Ninja Personal"
			)
			time.sleep(15)

	def cancel(self):
		self.finish()
	def finish(self):
		self.running = False

DiscordNinja().start()
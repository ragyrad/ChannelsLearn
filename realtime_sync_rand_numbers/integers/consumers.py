import json
import time
from random import randint

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
	def connect(self):
		self.accept()

		for i in range(1000):
			self.send(json.dumps({'message': randint(1, 100)}))
			time.sleep(1)
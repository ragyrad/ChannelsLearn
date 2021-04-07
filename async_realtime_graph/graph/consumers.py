import json
import asyncio
from random import randint

from channels.generic.websocket import AsyncWebsocketConsumer


class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        for i in range(1000):
            await self.send(json.dumps({'value': randint(-20, 20)}))
            await asyncio.sleep(1)

#server.py
import base64
import aiohttp
import asyncio
import websockets
from PIL import Image
from datetime import datetime
from io import BytesIO

async def hello(websocket, path):
    data = await websocket.recv()
    if len(data) < 20:
        print(f"< {data}")
        greeting = f"Hello {data}!"
        await websocket.send(greeting)
    else:
        print(len(data))
        im = Image.open(BytesIO(data))
        im.save('image.png', 'PNG')
        await websocket.send('Hell yes my friend')

start_server = websockets.serve(hello, "0.0.0.0", 5432)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

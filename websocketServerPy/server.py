#server.py
import asyncio
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

start_server = websockets.serve(hello, "0.0.0.0", 5432)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

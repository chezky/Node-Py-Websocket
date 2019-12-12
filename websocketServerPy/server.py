#server.py
import asyncio
import websockets

async def hello(websocket, path):
    data = await websocket.recv()
    if len(data) < 20:
        print(f"< {data}")
        greeting = f"Hello {data}!"
        await websocket.send(greeting)
        print(f"> {greeting}")
    else:
        await websocket.send('bytes!')


start_server = websockets.serve(hello, "0.0.0.0", 5432)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

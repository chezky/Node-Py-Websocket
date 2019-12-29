#server.py
import aiohttp
import asyncio
import websockets
from fastai import *
from fastai.vision import *
from io import BytesIO
from pathlib import Path

model_file_url = 'https://www.dropbox.com/s/6bgq8t6yextloqp/export.pkl?raw=1'
model_file_name = 'export.pkl'

path = Path(__file__).parent

async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f:
                f.write(data)

async def setup_learner():
    print('downloading')
    await download_file(model_file_url, path / model_file_name)
    try:
        learn = load_learner(path, model_file_name)
        print('loaded')
        return learn
    except RuntimeError as e:
        if len(e.args) > 0 and 'CPU-only machine' in e.args[0]:
            print(e)
            message = "\n\nThis model was trained with an old version of fastai and will not work in a CPU environment.\n\nPlease update the fastai library in your training environment and export your model again.\n\nSee instructions for 'Returning to work' at https://course.fast.ai."
            raise RuntimeError(message)
        else:
            raise

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_learner())]
learn = asyncio.get_event_loop().run_until_complete(asyncio.gather(*tasks))[0]

async def hello(websocket, path):
    data = await websocket.recv()
    if isinstance(data, str):
        print(f"< {data}")
        greeting = f"Hello {data}!"
        await websocket.send(greeting)
    else:
        img = open_image(BytesIO(data))
        prediction = learn.predict(img)[0]
        await websocket.send(str(prediction))

start_server = websockets.serve(hello, "0.0.0.0", 5432)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

"# Node-Py-Websocket"

After cloning:

```
cd websocketClient
docker build -t node-websocket-client .
cd ..
cd websocketServerPy
docker build -t python-websocket-server .
cd..
docker-compose up
```
if you are using docker-toolbox, and want to go to localhost:8000 to see your webserver,
go to 192.168.99.100:8000

# Node-Py-Webosckets

A base starter template for developing a web application in node, with a websocket link to a python container. Feature complete for deploying a Fastai model, without writing the server in python.

### Prerequisites

* [Docker](https://docs.docker.com/docker-for-windows/install/)
* [Node](https://nodejs.org/en/download/)
* [Python-3](https://www.python.org/downloads/)

### Installing

Clone the repository
```
cd websocketClient
docker build -t node-websocket-client .
cd ..
cd websocketServerPy
docker build -t python-websocket-server .
cd..
docker-compose up
```


## Running the tests

Open a browser and navigate to localhost:8000 or 192.168.99.100:8000 if you are using Docker-toolbox. If all is running properly you should see an option to upload an image. Wait a few minutes for the model to download. Upload an image, submit, and check the console to see your result.

## Notes

* To download latest [pytorch wheel images](https://download.pytorch.org/whl/cpu/torch_stable.html)<br/>
To use your own model, replace ```model_file_url``` to your own download link.

## Authors

* **Chezky Felsen** - *Author*

## License

This project is licensed under the ISC License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to [this repo](https://github.com/render-examples/fastai-v3) - Helpful starting point

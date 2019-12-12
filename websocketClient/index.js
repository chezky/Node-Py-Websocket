// //index.js
const express = require('express');
var bodyParser = require('body-parser');
const WebSocket = require('ws');
const address = 'ws://python:5432';

console.log('ready to send to ' + address);

app = express();

app.use(bodyParser.json());
app.use(express.static(__dirname + '/public' ));

app.get('/', (req, res) => {
    res.render('index');
})

app.post('/search', (req, res) => {
    var ws = new WebSocket(address);

    ws.on('open', function open() {
        ws.send(req.body.search);
    });

    ws.on('message', function incoming(data) {
      console.log(data);
      res.send(data);
    });
})

app.listen(process.env.PORT || 8000);

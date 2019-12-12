// //index.js
const WebSocket = require('ws');

const address = 'ws://python:5432'

const ws = new WebSocket(address);

console.log('ready to send to ' + address)

ws.on('open', function open() {
  ws.send('Chezky');
});

ws.on('message', function incoming(data) {
  console.log(data);
});

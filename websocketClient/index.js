// //index.js
const express = require('express');
var bodyParser = require('body-parser');
const WebSocket = require('ws');
const address = 'ws://localhost:5432';
var fs = require("fs");
const multer = require("multer");

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
const upload = multer({
  dest: "./uploads"
});

app.post('/uploadimage', upload.single("pic"),(req, res) => {
    const tempPath = req.file.path;
    console.log(tempPath);
    fs.readFile(tempPath, function(err, data) {
        if (err) throw err;
        let buff = fs.readFileSync(tempPath);
        let base64data = buff.toString('base64');
        // console.log('Image converted to base 64 is:\n\n' + base64data);
        // new Buffer.from(tempPath).toString('base64');
        var encodedImage = Buffer.alloc(base64data.length, base64data, 'base64');
        console.log('image byte length is : ' + base64data.length);
        var ws = new WebSocket(address);

        ws.on('open', function open() {
            ws.send(encodedImage);
        });

        ws.on('message', function incoming(data) {
          console.log(data);
          res.send(data);
        });
    });
})

app.listen(process.env.PORT || 8000);

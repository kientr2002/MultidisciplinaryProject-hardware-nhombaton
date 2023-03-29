const mqtt = require('mqtt');
const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);

const MQTT_SERVER = "mqtt.ohstem.vn";
const MQTT_PORT = 1883;
const MQTT_USERNAME = "nhombaton";
const MQTT_PASSWORD = "";
const link = "nhombaton/feeds/";
const list_feed = [
  "V1",
  "V2",
  "V3",
  "V4",
  "V10",
  "V12",
  "V13",
  "V14",
  "V15",
  "V16"
];

const client = mqtt.connect(`mqtt://${MQTT_SERVER}:${MQTT_PORT}`, {
  username: MQTT_USERNAME,
  password: MQTT_PASSWORD
});

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  console.log('a user connected');
});

server.listen(3000, () => {
  console.log('listening on *:3000');
});

client.on('connect', () => {
  console.log('Ket noi thanh cong');
  for (const feed of list_feed) {
    client.subscribe(link + feed, (err) => {
      if (err) {
        console.error(err);
      } else {
       //NOTHING
      }
    });
  }
});

client.on('message', (topic, message) => {
  console.log(`Nhan du lieu: ${topic.toString()} ${message.toString()}`);
  
});




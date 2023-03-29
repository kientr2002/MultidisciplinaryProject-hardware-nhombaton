const mqtt = require('mqtt');

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
  console.log(`Nhan du lieu: ${message.toString()}`);
  
});

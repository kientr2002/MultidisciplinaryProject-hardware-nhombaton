const mqtt = require('mqtt');

const MQTT_SERVER = "mqtt.ohstem.vn";
const MQTT_PORT = 1883;
const MQTT_USERNAME = "test1";
const MQTT_PASSWORD = "";
const link = "test1/feeds/";
const list_feed = [
  "V1"
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
        console.log(`Feed ${link}${feed} da duoc subscribe`);
      }
    });
  }
});

client.on('message', (topic, message) => {
  console.log(`Nhan du lieu: ${message.toString()}`);
  
});

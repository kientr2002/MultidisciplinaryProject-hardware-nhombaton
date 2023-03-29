import sys
import random
import time
import serial.tools.list_ports
import paho.mqtt.client as mqtt

import json
import requests

from Adafruit_IO import MQTTClient

# url web
url = "http://localhost/Multidisciplinary/Data/"

# mqtt ohstem
MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "nhombaton"
MQTT_PASSWORD = ""
link = "nhombaton/feeds/"
list_feed = [
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
]


# functional
def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)

def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload)

def mqtt_connected(client, userdata, flags, rc):
    for feed in list_feed:
        client.subscribe(link + feed)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    pass

def mqtt_disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(5)

def send_data_to_web(feed_id, value):
    data = {"feed_id": feed_id, "value": value}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        print("Data sent successfully.")
    else:
        print("Failed to send data.")

def on_message(client, userdata, message):
    print(str(message.topic)[16:] + ":" + str(message.payload.decode("utf-8")))
    value = str(message.payload.decode("utf-8"))
    feed_id = str(message.topic)[16:]
    send_data_to_web(feed_id, value)

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.on_message = on_message

mqttClient.loop_start()

while True:
    pass


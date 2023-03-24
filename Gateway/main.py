import sys
import random
import time
import serial . tools . list_ports
import paho.mqtt.client as mqtt

import json
import requests

from Adafruit_IO import MQTTClient

#url web


#mqtt ohstem
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
    "V11"
]
localtime = time.asctime( time.localtime(time.time()) )

# functional
def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)

def mqtt_connected(client, userdata, flags, rc):
    for feed in list_feed:
        client.subscribe(link + feed)

def mqtt_subscribed(client, userdata, mid, granted_qos):
   print("feed ohstem",mid,"subscribe thanh cong ...")

def mqtt_disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (5)
value = ""
def on_message(client, userdata, message):
    print(localtime, ":", str(message.topic)[16:] + ":" + str(message.payload.decode("utf-8")))
    value = str(message.payload.decode("utf-8"))
    

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.on_message = on_message

mqttClient.loop_start()

while True:
    pass

#Import package
import paho.mqtt.client as mqtt
import json
import time
import serial .tools .list_ports
import random
import sys
from datetime import datetime



#Connect to server
MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "nhombaton"
MQTT_PASSWORD = ""

#Feed data
TEMP = "nhombaton/feeds/V1"
HUMI = "nhombaton/feeds/V2"
SOIL_HUMI = "nhombaton/feeds/V3"
LIGHT = "nhombaton/feeds/V4"
LED = "nhombaton/feeds/V10"
PUMP = "nhombaton/feeds/V11"


#Message variables
temp = ""
humi = ""
soil_humi = ""
light = ""
led = ""
pump = ""
isMicrobitConnected = False

def connect(client):
    print("Ket noi thanh cong...")
    client.subcrible(TEMP)

def  subscribe(client , userdata , mid , granted_qos):
    print("Subcribe thanh cong...")
def  disconnected(client):
    print("Ngat ket noi...")
    sys.exit (1)
def  message(client , feed_id , payload):
    print("Nhan du lieu: " + payload)
    if isMicrobitConnected:
        serial.write((str(payload) + "#").encode())

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)

mqttClient.on_connect = connect
mqttClient.on_subscribe = subscribe

mqttClient.loop_start()
counter = 0 

while True:
    time.sleep(1)

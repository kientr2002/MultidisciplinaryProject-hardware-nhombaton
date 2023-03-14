#Import package
import paho.mqtt.client as mqtt
import json
import time
import serial.tools.list_ports
import random
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


def subscribed(client, userdata, flags, rc):
    print("Subscribed...")


while True:
    time.sleep(1)

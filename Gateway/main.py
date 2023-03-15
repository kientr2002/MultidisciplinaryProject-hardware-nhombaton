import sys
import random
import time
import serial . tools . list_ports
import paho.mqtt.client as mqtt

from Adafruit_IO import MQTTClient

#Adafruit_io
AIO_FEED_IDS = ["farm-button-led", "farm-button-pump", "farm-humi", "farm-light", "farm-soil-humi", "farm-temp"]
AIO_USERNAME = "teambaton"
AIO_KEY = "aio_Jsbj78KF7pj7sgelX7K8C9M6Ljnc"

#mqtt ohstem
MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "nhombaton"
MQTT_PASSWORD = ""
MQTT_TOPIC_TEMP = "nhombaton/feeds/V1"
MQTT_TOPIC_HUMI = "nhombaton/feeds/V2"
MQTT_TOPIC_SOIL_HUMI = "nhombaton/feeds/V3"
MQTT_TOPIC_LIGHT = "nhombaton/feeds/V4"
MQTT_TOPIC_PUMP = "nhombaton/feeds/V10"
MQTT_TOPIC_LED = "nhombaton/feeds/V11"


# functional

def connected(client):
    for feed in AIO_FEED_IDS:
        client.subscribe(feed)
    
def mqtt_connected(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC_TEMP)
    client.subscribe(MQTT_TOPIC_HUMI)
    client.subscribe(MQTT_TOPIC_SOIL_HUMI)
    client.subscribe(MQTT_TOPIC_LIGHT)
    client.subscribe(MQTT_TOPIC_PUMP)
    client.subscribe(MQTT_TOPIC_LED)
def subscribe(client , userdata , mid , granted_qos):
    print("feed ada",mid,"subscribe thanh cong ...")

def mqtt_subscribed(client, userdata, mid, granted_qos):
   print("feed ohstem",mid,"subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("!"+feed_id + ":" + payload + "#")


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.loop_start()

while True:
    pass
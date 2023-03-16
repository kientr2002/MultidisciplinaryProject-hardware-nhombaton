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
link = "nhombaton/feeds/"
list_feed = [
    "V1",
    "V2",
    "V3",
    "V4",
    "V10",
    "V11"
]

# functional
def mqtt_connected(client, userdata, flags, rc):
    for feed in list_feed:
        client.subscribe(link + feed)

def mqtt_subscribed(client, userdata, mid, granted_qos):
   print("feed ohstem",mid,"subscribe thanh cong ...")

def mqtt_disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (5)

def on_message(client, userdata, message):
    print(str(message.topic)[16:] + ":" + str(message.payload.decode("utf-8")))

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.on_message = on_message

mqttClient.loop_start()
counter = 0


while True:
    # print("Nhap du lieu ma ban muon thay doi (1 la pump, 2 la led):")
    # type_input = input()
    # value = 0
    # if type_input == 1:
    #     print("Nhap du lieu pump:")
    #     value = input()
    #     mqttClient.publish("nhombaton/feeds/V10",value)
    # elif type_input == 2:
    #     print("Nhap du lieu gia tri LED:")
    #     value = input()
    #     mqttClient.publish("nhombaton/feeds/V11",value)
    # print("Da cap nhat du lieu")
    pass
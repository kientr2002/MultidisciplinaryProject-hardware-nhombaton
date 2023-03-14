import paho.mqtt.client as mqtt





MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "nhombaton"
MQTT_PASSWORD = ""
TEMP = "nhombaton/feeds/V1"
HUMI = "nhombaton/feeds/V2"
SOIL_HUMI = "nhombaton/feeds/V3"
LIGHT = "nhombaton/feeds/V4"
LED = "nhombaton/feeds/V10"
PUMP = "nhombaton/feeds/V11"

def mqtt_connected(client, userdata, flags, rc):
    print("Connected succesfully!!")
    client.subscribe(TEMP)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)

#Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed

mqttClient.loop_start()
counter = 0


while True:
    pass
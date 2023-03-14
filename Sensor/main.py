from mqtt import *
from machine import RTC
import ntptime
import time
from aiot_lcd1602 import LCD1602
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from event_manager import *
from aiot_rgbled import RGBLed
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20

aiot_lcd1602 = LCD1602()

event_manager.reset()

def on_mqtt_message_receive_callback__V11_(th_C3_B4ng_tin):
  global HOUR, START, RT, MINUTE, SET_LED, RH, SET_PUMP, SM, LUX
  if th_C3_B4ng_tin == '1':
    SET_LED = 1
  else:
    SET_LED = 0

def on_mqtt_message_receive_callback__V10_(th_C3_B4ng_tin):
  global HOUR, START, RT, MINUTE, SET_LED, RH, SET_PUMP, SM, LUX
  if th_C3_B4ng_tin == '1':
    SET_PUMP = 1
  else:
    SET_PUMP = 0

# Mô tả hàm này...
def _C4_90_C4_83ng_k_C3_BD_server():
  global th_C3_B4ng_tin, HOUR, START, RT, MINUTE, SET_LED, RH, SET_PUMP, SM, LUX, aiot_dht20, tiny_rgb, aiot_lcd1602
  mqtt.on_receive_message('V11', on_mqtt_message_receive_callback__V11_)
  mqtt.on_receive_message('V10', on_mqtt_message_receive_callback__V10_)

tiny_rgb = RGBLed(pin0.pin, 4)

# Mô tả hàm này...
def B_E1_BA_ADt__C4_91_C3_A8n():
  global th_C3_B4ng_tin, HOUR, START, RT, MINUTE, SET_LED, RH, SET_PUMP, SM, LUX, aiot_dht20, tiny_rgb, aiot_lcd1602
  if (round(translate((pin0.read_analog()), 0, 4095, 0, 100))) <= 20:
    tiny_rgb.show(0, hex_to_rgb('#ff0000'))

# Mô tả hàm này...
def B_E1_BA_ADt_m_C3_A1y_b_C6_A1m():
  global th_C3_B4ng_tin, HOUR, START, RT, MINUTE, SET_LED, RH, SET_PUMP, SM, LUX, aiot_dht20, tiny_rgb, aiot_lcd1602
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) <= 10:
    pin10.write_analog(round(translate(90, 0, 100, 0, 1023)))
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) > 10 and (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) <= 20:
    pin10.write_analog(round(translate(80, 0, 100, 0, 1023)))
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) > 20 and (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) <= 30:
    pin10.write_analog(round(translate(70, 0, 100, 0, 1023)))
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) > 30 and (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) <= 40:
    pin10.write_analog(round(translate(60, 0, 100, 0, 1023)))
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) > 40 and (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) <= 50:
    pin10.write_analog(round(translate(50, 0, 100, 0, 1023)))

aiot_dht20 = DHT20(SoftI2C(scl=Pin(22), sda=Pin(21)))

def on_event_timer_callback_G_o_U_R_C():
  global th_C3_B4ng_tin, HOUR, START, RT, MINUTE, SET_LED, RH, SET_PUMP, SM, LUX
  aiot_dht20.read_dht20()
  RT = aiot_dht20.dht20_temperature()
  RH = aiot_dht20.dht20_humidity()
  SM = round(translate((pin1.read_analog()), 0, 4095, 0, 100))
  LUX = round(translate((pin2.read_analog()), 0, 4095, 0, 100))
  aiot_lcd1602.move_to(0, 0)
  aiot_lcd1602.putstr('RT:')
  aiot_lcd1602.move_to(3, 0)
  aiot_lcd1602.putstr(RT)
  aiot_lcd1602.move_to(7, 0)
  aiot_lcd1602.putstr('*C')
  aiot_lcd1602.move_to(10, 0)
  aiot_lcd1602.putstr('RH:')
  aiot_lcd1602.move_to(13, 0)
  aiot_lcd1602.putstr(RH)
  aiot_lcd1602.move_to(15, 0)
  aiot_lcd1602.putstr('%')
  aiot_lcd1602.move_to(0, 1)
  aiot_lcd1602.putstr('LUX:')
  aiot_lcd1602.move_to(4, 1)
  aiot_lcd1602.putstr(LUX)
  aiot_lcd1602.move_to(6, 1)
  aiot_lcd1602.putstr('%')
  aiot_lcd1602.move_to(9, 1)
  aiot_lcd1602.putstr('SM:')
  aiot_lcd1602.move_to(13, 1)
  aiot_lcd1602.putstr(SM)
  aiot_lcd1602.move_to(15, 1)
  aiot_lcd1602.putstr('%')
  mqtt.publish('V1', RT)
  mqtt.publish('V2', RH)
  mqtt.publish('V3', SM)
  mqtt.publish('V4', LUX)

event_manager.add_timer_event(5000, on_event_timer_callback_G_o_U_R_C)

def on_event_timer_callback_x_b_c_I_Q():
  global th_C3_B4ng_tin, HOUR, START, RT, MINUTE, SET_LED, RH, SET_PUMP, SM, LUX
  HOUR = int(('%0*d' % (2, RTC().datetime()[4])))
  MINUTE = int(('%0*d' % (2, RTC().datetime()[5])))
  if HOUR == 5 and MINUTE == 0 or HOUR == 17 and MINUTE == 30:
    B_E1_BA_ADt_m_C3_A1y_b_C6_A1m()
  else:
    if SET_PUMP == 1:
      B_E1_BA_ADt_m_C3_A1y_b_C6_A1m()
    else:
      pin10.write_analog(round(translate(0, 0, 100, 0, 1023)))
  if HOUR >= 17 and HOUR <= 6:
    B_E1_BA_ADt__C4_91_C3_A8n()
  else:
    if SET_LED == 1:
      B_E1_BA_ADt__C4_91_C3_A8n()
    else:
      tiny_rgb.show(0, hex_to_rgb('#000000'))

event_manager.add_timer_event(5000, on_event_timer_callback_x_b_c_I_Q)

if True:
  mqtt.connect_wifi('locton', '10k1tieng')
  mqtt.connect_broker(server='mqtt.ohstem.vn', port=1883, username='nhombaton', password='')
  ntptime.settime()
  (year, month, mday, week_of_year, hour, minute, second, milisecond) = RTC().datetime()
  RTC().init((year, month, mday, week_of_year, hour+7, minute, second, milisecond))
  aiot_lcd1602.clear()
  SET_PUMP = 0
  START = 0
  _C4_90_C4_83ng_k_C3_BD_server()
  display.scroll('AIOT')

while True:
  if button_a.is_pressed():
    START = (START if isinstance(START, (int, float)) else 0) + 1
  if START == 1:
    event_manager.run()
    mqtt.check_message()
    time.sleep_ms(1000)

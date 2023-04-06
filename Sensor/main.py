from mqtt import *
from machine import RTC
import ntptime
import time
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
from aiot_rgbled import RGBLed
from aiot_lcd1602 import LCD1602
from event_manager import *
from machine import Pin, SoftI2C
from aiot_dht20 import DHT20

tiny_rgb = RGBLed(pin0.pin, 4)

aiot_lcd1602 = LCD1602()

event_manager.reset()

def on_mqtt_message_receive_callback__V12_(th_C3_B4ng_tin):
  global HOUR, MINUTE, VAL_LED, VAL_PUMP_TC, RT, VAL_PUMP, RH, TURN_ON_SET, SET_PUMP, START, VAL_LED_TC, SM, LUX, SET_LED
  VAL_LED = int(th_C3_B4ng_tin)

def on_mqtt_message_receive_callback__V16_(th_C3_B4ng_tin):
  global HOUR, MINUTE, VAL_LED, VAL_PUMP_TC, RT, VAL_PUMP, RH, TURN_ON_SET, SET_PUMP, START, VAL_LED_TC, SM, LUX, SET_LED
  VAL_PUMP = int(th_C3_B4ng_tin)

def on_mqtt_message_receive_callback__V14_(th_C3_B4ng_tin):
  global HOUR, MINUTE, VAL_LED, VAL_PUMP_TC, RT, VAL_PUMP, RH, TURN_ON_SET, SET_PUMP, START, VAL_LED_TC, SM, LUX, SET_LED
  if th_C3_B4ng_tin == '1':
    TURN_ON_SET = 1
  else:
    TURN_ON_SET = 0

# Mô tả hàm này...
def _C4_90_C4_83ng_k_C3_BD_server():
  global HOUR, th_C3_B4ng_tin, MINUTE, VAL_LED, VAL_PUMP_TC, RT, VAL_PUMP, RH, TURN_ON_SET, SET_PUMP, START, VAL_LED_TC, SM, LUX, SET_LED, aiot_dht20, tiny_rgb, aiot_lcd1602
  mqtt.on_receive_message('V12', on_mqtt_message_receive_callback__V12_)
  mqtt.on_receive_message('V16', on_mqtt_message_receive_callback__V16_)
  mqtt.on_receive_message('V14', on_mqtt_message_receive_callback__V14_)

# Mô tả hàm này...
def B_E1_BA_ADt_m_C3_A1y_b_C6_A1m_t_E1_BB_B1__C4_91_E1_BB_99ng():
  global HOUR, th_C3_B4ng_tin, MINUTE, VAL_LED, VAL_PUMP_TC, RT, VAL_PUMP, RH, TURN_ON_SET, SET_PUMP, START, VAL_LED_TC, SM, LUX, SET_LED, aiot_dht20, tiny_rgb, aiot_lcd1602
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) <= 10:
    VAL_PUMP_TC = 100
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(0, hex_to_rgb('#ff0000'))
    pin10.write_analog(round(translate(100, 0, 100, 0, 1023)))
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) > 10 and (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) <= 20:
    VAL_PUMP_TC = 75
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(1, hex_to_rgb('#ff0000'))
    tiny_rgb.show(2, hex_to_rgb('#ff0000'))
    tiny_rgb.show(3, hex_to_rgb('#ff0000'))
    tiny_rgb.show(4, hex_to_rgb('#000000'))
    pin10.write_analog(round(translate(75, 0, 100, 0, 1023)))
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) > 20 and (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) <= 30:
    VAL_PUMP_TC = 50
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(2, hex_to_rgb('#ff0000'))
    tiny_rgb.show(1, hex_to_rgb('#ff0000'))
    tiny_rgb.show(3, hex_to_rgb('#000000'))
    tiny_rgb.show(4, hex_to_rgb('#000000'))
    pin10.write_analog(round(translate(50, 0, 100, 0, 1023)))
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) > 30 and (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) <= 50:
    VAL_PUMP_TC = 25
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(4, hex_to_rgb('#000000'))
    tiny_rgb.show(1, hex_to_rgb('#ff0000'))
    tiny_rgb.show(2, hex_to_rgb('#000000'))
    tiny_rgb.show(3, hex_to_rgb('#000000'))
    pin10.write_analog(round(translate(25, 0, 100, 0, 1023)))
  if (round(translate((pin1.read_analog()), 0, 4095, 0, 100))) > 50:
    VAL_PUMP_TC = 0
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(0, hex_to_rgb('#000000'))
    pin10.write_analog(round(translate(0, 0, 100, 0, 1023)))

# Mô tả hàm này...
def B_E1_BA_ADt__C4_91_C3_A8n_t_E1_BB_B1__C4_91_E1_BB_99ng():
  global HOUR, th_C3_B4ng_tin, MINUTE, VAL_LED, VAL_PUMP_TC, RT, VAL_PUMP, RH, TURN_ON_SET, SET_PUMP, START, VAL_LED_TC, SM, LUX, SET_LED, aiot_dht20, tiny_rgb, aiot_lcd1602
  if (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) <= 10:
    display.set_all('#ffffff')
    display.set_brightness(100)
    VAL_LED_TC = 100
    mqtt.publish('V13', VAL_LED_TC)
  if (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) > 10 and (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) <= 20:
    display.set_all('#ffffff')
    display.set_brightness(90)
    VAL_LED_TC = 90
    mqtt.publish('V13', VAL_LED_TC)
  if (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) > 20 and (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) <= 30:
    display.set_all('#ffffff')
    display.set_brightness(80)
    VAL_LED_TC = 80
    mqtt.publish('V13', VAL_LED_TC)
  if (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) > 30 and (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) <= 40:
    display.set_all('#ffffff')
    display.set_brightness(70)
    VAL_LED_TC = 70
    mqtt.publish('V13', VAL_LED_TC)
  if (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) > 40 and (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) <= 50:
    display.set_all('#ffffff')
    display.set_brightness(50)
    VAL_LED_TC = 50
    mqtt.publish('V13', VAL_LED_TC)
  if (round(translate((pin2.read_analog()), 0, 4095, 0, 100))) > 50:
    display.set_all('#000000')
    VAL_LED_TC = 0
    mqtt.publish('V13', VAL_LED_TC)

aiot_dht20 = DHT20(SoftI2C(scl=Pin(22), sda=Pin(21)))

def on_event_timer_callback_G_o_U_R_C():
  global HOUR, th_C3_B4ng_tin, MINUTE, VAL_LED, VAL_PUMP_TC, RT, VAL_PUMP, RH, TURN_ON_SET, SET_PUMP, START, VAL_LED_TC, SM, LUX, SET_LED
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
  aiot_lcd1602.putstr('LIG:')
  aiot_lcd1602.move_to(4, 1)
  aiot_lcd1602.putstr(LUX)
  aiot_lcd1602.move_to(6, 1)
  aiot_lcd1602.putstr('LX')
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
  print((''.join([str(x) for x in ['!', 'T:', aiot_dht20.dht20_temperature(), '-', 'H:', aiot_dht20.dht20_humidity(), '-', 'S:', round(translate((pin1.read_analog()), 0, 4095, 0, 100)), '-', 'L:', round(translate((pin2.read_analog()), 0, 4095, 0, 100)), '#']])), end =' ')

event_manager.add_timer_event(5000, on_event_timer_callback_G_o_U_R_C)

def on_event_timer_callback_x_b_c_I_Q():
  global HOUR, th_C3_B4ng_tin, MINUTE, VAL_LED, VAL_PUMP_TC, RT, VAL_PUMP, RH, TURN_ON_SET, SET_PUMP, START, VAL_LED_TC, SM, LUX, SET_LED
  if TURN_ON_SET == 1:
    display.set_all('#ffffff')
    display.set_brightness(VAL_LED)
    VAL_LED_TC = VAL_LED
    mqtt.publish('V13', VAL_LED_TC)
    B_E1_BA_ADt_m_C3_A1y_b_C6_A1m_th_E1_BB_A7_c_C3_B4ng()
  else:
    B_E1_BA_ADt__C4_91_C3_A8n_t_E1_BB_B1__C4_91_E1_BB_99ng()
    B_E1_BA_ADt_m_C3_A1y_b_C6_A1m_t_E1_BB_B1__C4_91_E1_BB_99ng()

event_manager.add_timer_event(100, on_event_timer_callback_x_b_c_I_Q)

# Mô tả hàm này...
def B_E1_BA_ADt_m_C3_A1y_b_C6_A1m_th_E1_BB_A7_c_C3_B4ng():
  global HOUR, th_C3_B4ng_tin, MINUTE, VAL_LED, VAL_PUMP_TC, RT, VAL_PUMP, RH, TURN_ON_SET, SET_PUMP, START, VAL_LED_TC, SM, LUX, SET_LED, aiot_dht20, tiny_rgb, aiot_lcd1602
  if VAL_PUMP == 0:
    VAL_PUMP_TC = 0
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(0, hex_to_rgb('#000000'))
    pin10.write_analog(round(translate(0, 0, 100, 0, 1023)))
  if VAL_PUMP == 25:
    VAL_PUMP_TC = 25
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(4, hex_to_rgb('#000000'))
    tiny_rgb.show(1, hex_to_rgb('#ff0000'))
    tiny_rgb.show(2, hex_to_rgb('#000000'))
    tiny_rgb.show(3, hex_to_rgb('#000000'))
    pin10.write_analog(round(translate(25, 0, 100, 0, 1023)))
  if VAL_PUMP == 50:
    VAL_PUMP_TC = 50
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(2, hex_to_rgb('#ff0000'))
    tiny_rgb.show(1, hex_to_rgb('#ff0000'))
    tiny_rgb.show(3, hex_to_rgb('#000000'))
    tiny_rgb.show(4, hex_to_rgb('#000000'))
    pin10.write_analog(round(translate(50, 0, 100, 0, 1023)))
  if VAL_PUMP == 75:
    VAL_PUMP_TC = 75
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(1, hex_to_rgb('#ff0000'))
    tiny_rgb.show(2, hex_to_rgb('#ff0000'))
    tiny_rgb.show(3, hex_to_rgb('#ff0000'))
    tiny_rgb.show(4, hex_to_rgb('#000000'))
    pin10.write_analog(round(translate(75, 0, 100, 0, 1023)))
  if VAL_PUMP == 100:
    VAL_PUMP_TC = 100
    mqtt.publish('V15', VAL_PUMP_TC)
    tiny_rgb.show(0, hex_to_rgb('#ff0000'))
    pin10.write_analog(round(translate(100, 0, 100, 0, 1023)))

if True:
  mqtt.connect_wifi('locton', '10k1tieng')
  mqtt.connect_broker(server='mqtt.ohstem.vn', port=1883, username='nhombaton', password='')
  ntptime.settime()
  (year, month, mday, week_of_year, hour, minute, second, milisecond) = RTC().datetime()
  RTC().init((year, month, mday, week_of_year, hour+7, minute, second, milisecond))
  SET_PUMP = 0
  TURN_ON_SET = 0
  SET_LED = 0
  START = 0
  display.set_all('#000000')
  tiny_rgb.show(0, hex_to_rgb('#000000'))
  pin10.write_analog(round(translate(0, 0, 100, 0, 1023)))
  aiot_lcd1602.clear()
  _C4_90_C4_83ng_k_C3_BD_server()
  display.scroll('AIOT')

while True:
  HOUR = int(('%0*d' % (2, RTC().datetime()[4])))
  MINUTE = int(('%0*d' % (2, RTC().datetime()[5])))
  if button_a.is_pressed():
    START = (START if isinstance(START, (int, float)) else 0) + 1
  if START >= 1:
    event_manager.run()
    mqtt.check_message()
    time.sleep_ms(1000)

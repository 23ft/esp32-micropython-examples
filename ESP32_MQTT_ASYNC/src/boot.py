from machine import Pin
import network
from utime import sleep_ms

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Sebas y felipe'
password = 'Manuelpipe1'
lamp1 = Pin(18, Pin.OUT, value = 0) # reset pin lamp 1
lamp2 = Pin(14, Pin.OUT, value = 0) # reset pin lamp 2
led_user = Pin(2, Pin.OUT, value = 1) # when is 1 describe conect to broker.

station = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)

ap.active(False)
station.active(False)
try:
  station.active(True)
  station.connect(ssid, password)
  print("[boot-debug] Connecting to WIFI ssid: ", ssid, "....")
except:
  print("[boot-debug] Error connecting to wifi, ssid: ", ssid, " password: ", password)
cont = 0

while not station.isconnected():
  led_user.value(not led_user.value())
  sleep_ms(100)  
  
led_user.value(0)

print('[boot-debug] Connected to', ssid)
print('[boot-debug] info connection is: ', station.ifconfig())

#import main
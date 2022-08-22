try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Sebas y felipe'
password = 'Manuelpipe1'

station = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
station.active(False)

gc.collect()
if station.active():
  station.active(False)
  station.active(True)
else:
  station.active(True)
  
gc.collect()
station.connect(ssid, password)

while not station.isconnected():
  pass

print('[boot-debug] Connected to', ssid)
print('[boot-debug] info connection is: ', station.ifconfig())


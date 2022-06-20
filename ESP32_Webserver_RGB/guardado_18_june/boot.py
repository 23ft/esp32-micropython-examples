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

ssid = 'Sebas y Felipe'
password = '@LSISENSSSNMYMS060201@'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Coneccion realizada.')
print(station.ifconfig())


#inisdadsd
relay = Pin(26, Pin.OUT)
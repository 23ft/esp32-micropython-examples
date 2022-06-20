"""
try:
  import usocket as socket
except:
  import socket
"""

from machine import Pin
from machine import unique_id
from umqttsimple import MQTTClient
import ubinascii
import network
import esp
import gc
import time

esp.osdebug(None)
gc.collect()

#ssid = 'ESTEBAN'
#password = 'E12345678'

ssid = 'Sebas y Felipe'
password = '@LSISENSSSNMYMS060201@'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

espid = ubinascii.hexlify(unique_id())

while station.isconnected() == False:
    pass

print('Conectado a internet! \n.')
print('Datos conexion = ', station.ifconfig())
print('Unique Id = ', espid)



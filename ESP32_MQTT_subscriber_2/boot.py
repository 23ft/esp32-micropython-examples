# This file is executed on every boot (including wake-boot from deepsleep)
#import webrepl
#webrepl.start()

import esp
import utime
import ubinascii
from machine import Pin, unique_id
import network

esp.osdebug(None)

"""
Conexion wifi
"""

# Internet
ssid = 'Sebas y Felipe'
password = '@LSISENSSSNMYMS060201@'

# instanciamos como STACION.
sta_if = network.WLAN(network.STA_IF)

# Activando STATION interfaz
sta_if.active(True)

# Conectando a wifi.
sta_if.connect(ssid, password)
print("boot")

while sta_if.isconnected() == False:
  pass


print("[Boot.py - NetworkConnect] Conectado a internet con extio!\n\n",
      "[Boot.py - NetworkConnect] Red conectado: ", ssid, "\n",
      "[Boot.py - NetworkConnect] Informacion conexion: ", sta_if.ifconfig())

"""
 Datos globales conexion MQTT
"""

mqtt_id = ubinascii.hexlify(unique_id())
mqtt_host = "192.168.0.31" 
mqtt_port = 1883
mqtt_user = ""
mqtt_pass = ""

"""
 Configuracion Pines
"""

led_esp = Pin(2, Pin.OUT)


from machine import Pin
from utime import sleep

z44pin = Pin(4, Pin.OUT)

while(1):
    print("On mosfet..\n")
    z44pin.value(1)
    sleep(10)
    print("OFF mosfet..\n")
    z44pin.value(0)
    sleep(10)
    
    
     
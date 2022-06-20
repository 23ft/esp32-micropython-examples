from machine import Pin, I2C
from BMP280 import BMP280
from utime import sleep


SDA = Pin(21)
SCL = Pin(22)

bmpBus = I2C(0, scl=SCL, sda=SDA)

bmpObj = BMP280(bmpBus)


while True:
    #bmpObj.get()
    
    temp = bmpObj.getTemp()
    press = bmpObj.getPress()
    alt = bmpObj.getAltitude()
    
    print("Tempratura: ", temp, "\nPresion: ", press,"\nAltitude: ", alt, "\n\n")
    sleep(1)
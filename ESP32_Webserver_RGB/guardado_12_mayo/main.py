from machine import Pin, PWM
from time import sleep

class RGB:
    def __init__(self):
        self.frec = 1000
        self.green = PWM(Pin(5), self.frec)
        self.red = PWM(Pin(18), self.frec)
        self.blue = PWM(Pin(19), self.frec)


    def color1(self): # Algo asi como un gris.
        cont = 0
        while cont < 10:
            self.green.duty(50)
            self.red.duty(40)
            self.blue.duty(120)
            cont += 1
            sleep(1)
            print(cont)
        self.green.duty(0)
        self.red.duty(0)
        self.blue.duty(0)
    
    def Sec1(self):
        while True:
            print('\n Secuecnia 1\n')
            green = self.green
            red = self.red
            blue = self.blue
            
            green.duty(255)
            red.duty(0)
            blue.duty(255)
            sleep(1)
            green.duty(127)
            red.duty(127)
            blue.duty(127)
            sleep(1)    
            green.duty(0)
            red.duty(255)
            blue.duty(0)
            sleep(1)

                         
tira = RGB()
tira.color1()
sec1 = tira.Sec1()

if sec1 == True:
    print('Saliendo programa')
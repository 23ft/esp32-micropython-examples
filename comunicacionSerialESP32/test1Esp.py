from machine import Pin, UART
import time

class Machine():
    def __init__(self):
        self.ldred = Pin(13, Pin.OUT)
        self.ldyell = Pin(12, Pin.OUT)
        self.ldgre = Pin(14, Pin.OUT)
                
    def stateZero(self):
        # state 0, red set and yel, gre is reset
        self.ldgre.value(0)
        self.ldred.value(1)
        self.ldyell.value(0)
        
        time.sleep(3)
        self.stateOne()
    
    def stateOne(self):
        # state 1, red set and yell set, gree reset.
        self.ldgre.value(0)
        self.ldred.value(1)
        self.ldyell.value(1)
        
        time.sleep(0.5)
        self.stateTwo()
        
    def stateTwo(self):
        # state 2, green is set, red and yell is reset.
        self.ldgre.value(1)
        self.ldred.value(0)
        self.ldyell.value(0)
        
        # time for state green.
        time.sleep(5)
        self.stateThre()
        
    def stateThre(self):
        self.ldgre.value(1)
        self.ldred.value(0)
        self.ldyell.value(1)
        
        time.sleep(0.5)
        
    def motoMachine(self):
        while True:
            self.stateZero()
            time.sleep(0.5)
            print("pepe")
                
maquina = Machine()
maquina.motoMachine()


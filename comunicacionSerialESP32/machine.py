from machine import Pin, UART
import time

class Machine():
    def __init__(self):
        self.ldred = Pin(14, Pin.OUT)
        self.ldyell = Pin(18, Pin.OUT)
        self.ldgre = Pin(19, Pin.OUT)
                
    def stateZero(self):
        # state 0, red set and yel, gre is reset
        self.ldgre = 0
        self.ldred = 1
        self.ldyell = 0
        
        time.sleep(3)
        self.stateOne()
    
    def stateOne(self):
        # state 1, red set and yell set, gree reset.
        self.ldgre = 0
        self.ldred = 1
        self.ldyell = 1
        
        time.sleep(0.5)
        self.stateTwo()
        
    def stateTwo(self):
        # state 2, green is set, red and yell is reset.
        self.ldgre = 1
        self.ldred = 0
        self.ldyell = 0
        
        # time for state green.
        time.sleep(3)
        self.stateThre()
        
    def stateThre(self):
        self.ldgre = 1
        self.ldred = 0
        self.ldyell = 1
        
        time.sleep(0.5)
        self.stateZero()
        
                    
    def motoMachine(self):
        while True:
            print("wait for init state...")
            print("[State 0]")
            self.x = int(input("~insert 1 to init: "))
            
            if self.x:
                self.x = 0
                self.stateOne();
                
                
maquina = Machine()
maquina.motoMachine()
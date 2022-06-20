from machine import Pin, Timer
import _thread
import utime


class prueba1():
    def __init__(self):
        self.vac = Pin(13, Pin.IN)
        self.vba = Pin(14, Pin.IN)
        self.vcb = Pin(12, Pin.IN)
        
        # Abatimiento
        self.s4 = Pin(2, Pin.OUT)
        self.s6 = Pin(4, Pin.OUT)
        self.s2 = Pin(5, Pin.OUT)
        
        # Elevacion
        self.s1 = Pin(18, Pin.OUT)
        self.s3 = Pin(19, Pin.OUT)
        self.s5 = Pin(21, Pin.OUT)
        
        #Timers
        
        self.tm0 = Timer(0)
        self.tm1 = Timer(1)
        self.tm2 = Timer(2)
        self.tm3 = Timer(3)
    
    # Metodos para conmutacion en bajada.
    def callBackFAC(self):
        self.s4 = not self.s4
    
    def callBackFBA(self):
        self.s6 = not self.s6
             
    def callBackFCB(self):
        self.s2 = not self.s2
    
    # Metodos para conmutacion en elevacion.    
    def callBackRAC(self):
        self.s1 = not self.s4
    
    def callBackRBA(self):
        self.s3 = not self.s6
             
    def callBackRCB(self):
        self.s5 = not self.s2
        
    # thread 0: esta pendiente cuando la señal del comparador esta en alto, suponiendo
    # que en este instante de tiempo donde se efectua el cambio la señal esta iniciando su amabtimiento.
    def modF(self):
        while(1):
            if (self.vac): # comparador bascula es high cuando esta en abatimiento.
                # ejecurcion timer 0  en un solo disparo.
                self.tm0.init(period=4.166e-3, mode=Timer.ONE_SHOT, callback=self.callBackFAC)
                
            if (self.vba):
                # ejecucion timer 1 en un solo dispario.
                self.tm1.init(period=4.166e-3, mode=Timer.ONE_SHOT, callback=self.callBackFBA)
                
            if (self.vcb):        
                pass
            
    def modR(self):
        _thread.start_new_thread(self.modF, ())
                
        while(1):
            if (not self.vac): # comparador bascula es high cuando esta en abatimiento.
                # ejecurcion timer 0  en un solo disparo.
                self.tm0.init(period=4.166e-3, mode=Timer.ONE_SHOT, callback=self.callBackRAC)
                
            if (not self.vba):
                # ejecucion timer 1 en un solo dispario.
                self.tm1.init(period=4.166e-3, mode=Timer.ONE_SHOT, callback=self.callBackRBA)
                
            if (not self.vcb):
                self.tm2.init(period=4.166e-3, mode=Timer.ONE_SHOT, callback=self.callBackRBA)        
                pass
      
from machine import Pin, Timer
import _thread
import utime
        
        # Abatimiento
s4 = Pin(4, Pin.OUT)
s6 = Pin(2, Pin.OUT)
s2 = Pin(5, Pin.OUT)
        
        # Elevacion
s1 = Pin(18, Pin.OUT)
s3 = Pin(19, Pin.OUT)
s5 = Pin(21, Pin.OUT)
        
class prueba1():
    def __init__(self):
        self.vac = Pin(13, Pin.IN)
        self.vba = Pin(14, Pin.IN)
        self.vcb = Pin(12, Pin.IN)
        
        self.tm0 = Timer(0)
        self.tm1 = Timer(1)
        self.tm2 = Timer(2)
        self.tm3 = Timer(3)
        
    # Metodos para conmutacion en bajada.
    def callBackFAC(self, time):
        global s4
        s4.value(not s4.value())
        #print("s4 shot")
        
    def callBackFBA(self, time):
        global s6
        s6.value(not s6.value())    
    
    def callBackFCB(self, time):
        global s2
        s2.value(not s2.value())
    
    # Metodos para conmutacion en elevacion.    
    def callBackRAC(self, timer):
        global s1
        s1.value(not s1.value())
    
    def callBackRBA(self, timer):
        global s3
        s3.value(not s3.value())     
    
    def callBackRCB(self, timer):
        global s5
        s5.value(not s5.value())
        
    # thread 0: esta pendiente cuando la señal del comparador esta en alto, suponiendo
    # que en este instante de tiempo donde se efectua el cambio la señal esta iniciando su amabtimiento.
    def modF(self):
        
        while(1):
            if (self.vac.value()): # comparador bascula es high cuando esta en abatimiento.
                # ejecurcion timer 0  en un solo disparo.
                self.tm0.init(period=4, mode=Timer.ONE_SHOT, callback=self.callBackFAC)
                #print("contador abatimiento inciado...\n")
            """    
            if (self.vba):
                # ejecucion timer 1 en un solo dispario.
                self.tm1.init(period=1, mode=Timer.ONE_SHOT, callback=self.callBackFBA)
                
            if (self.vcb):
                self.tm2.init(period=1, mode=Timer.ONE_SHOT, callback=self.callBackFCB)
            """    
            
    def modR(self):
        global s1,s2,s3,s4,s5,s6
        s1.value(0)
        s2.value(0)
        s3.value(0)
        s4.value(0)
        s5.value(0)
        s6.value(0)
        _thread.start_new_thread(self.modF, ())
        
        
        while(1):
            if (not self.vac.value()): # comparador bascula es high cuando esta en abatimiento.
                # ejecurcion timer 0  en un solo disparo.
                self.tm0.init(period=4, mode=Timer.ONE_SHOT, callback=self.callBackRAC)
            """    
            if (not self.vba):
                # ejecucion timer 1 en un solo dispario.
                self.tm1.init(period=1, mode=Timer.ONE_SHOT, callback=self.callBackRBA)
                
            if (not self.vcb):
                self.tm2.init(period=1, mode=Timer.ONE_SHOT, callback=self.callBackRCB)        
            """                
prueba = prueba1()
prueba.modR()



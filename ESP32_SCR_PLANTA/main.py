from machine import Pin, ADC
from utime import sleep_us

class SCRPlanta():
    def __init__(self):
        
        self.pin_voltaje = Pin(19, Pin.IN)
        
        self.pulse = Pin(18, Pin.OUT)
        self.button = Pin(15, Pin.IN)
        
        self.scr_120 = Pin(16,Pin.OUT)
        self.scr_150 = Pin(4,Pin.OUT)
        self.scr_act = "0"
        
        self.SCR = {"120":self.scr_120,
                    "150":self.scr_150}
        
        self.mod1 = Pin(33, Pin.OUT) # 120V
        self.mod2 = Pin(32, Pin.OUT) # 150V
        
        
    def read(self):
        return 
        
    def mainADC(self):
        while True:
            data = 0
            for x in range(0,10,1):
                data += self.adc.read()
            data = data / 10     
            #print("puls, data is: ", type(data))
            if ((data >= 2000) and (data <= 2072)):
                #print("puls, data is: ", data)
                self.pulse.value(1)
                sleep_us(100)
                self.pulse.value(0)
                
    def mainCOMP(self):
        """
            solucion 1:
            
            * configuracion salida comparador para dos entradas
            * asignacion IRQ para un pin en flancos en accenso, y otro flancos en bajada.
            
            solucion 2:
            
            * ingresa a bucle deteccion elevacion, abatimiento, una ves entre a estos
            dos estados anteriores se mantendra un FLAG sobre el modo actual para iniciar
            otro bucle con este mismo, en este mismo dependiendo el caso cambiara 
            
        """
        self.fallingMode = False
        self.rasingMode = False
        self.scr_act = "0"
        self.cont_btn = 0
        
        self.scr_120.value(0)
        self.scr_150.value(0)
        
        # Main program.
        while True:
            if(not self.button.value()):
                """
                    * Anti rebote algorithm:
                        -> BUtton en configuracion PULL-UP
                        -> Se realiza deteccion de estado LOW, una vez se realiza la deteccion
                        se hace polling para determinar cada < 50us*1300veces > el valor de la señal (se aumenta un contador cada vez que sea LOW)
                        -> una vez relizado el sondeo se valida que si el valor es mayor a 700 (valor ajustado en practica) ejecute el cambio.

                """
                # Anti rebote tipo polling.
                contdeb = 0
                for x in range(0, 1300, 1):
                    if(not self.button.value()):
                        contdeb += 1
                        sleep_us(40) # *El toggle lo detecta sin problemas con un sondeo cada 50us
                        # sleep_us(80) *El toggle se ve con delay ademas no es placentero el pulsar el botont
                
                # Seleccion estado boton.
                if(contdeb >= 700):
                
                    self.cont_btn += 1

                    if (self.cont_btn == 3):
                        self.cont_btn = 1

                    # Modes.
                     
                                
                    """ 
                        *Preguntar cual esta encendido y apagarlo cuando la señal de voltaje este en elevacion.
                        *Una vez apagado esperar a que la señal de voltaje pase a abatimiento, estando hay esperar
                        a corriente cruze en elevacion cuando cruza esperar 90us para encender nuevos SCRS.
                    """

                    # 120V    
                    if(self.cont_btn == 1):
                        
                        # Desconectar SCR activo.
                        
                        """
                            Verificar si es necesario apagar en rasing o si eso no importa.
                        """
                        if (self.scr_act == "0"):
                            pass
                        else:
                            while self.pin_voltaje.value():
                                # Wait for raising for power off SCR.
                                pass
                            
                            # Wait 10 us later detectd raising and verify with IF.
                            sleep_us(10)
                            if(not self.pin_voltaje.value()):
                                self.SCR[self.scr_act].value(0)
                        
                        # Esperar flanco elevacion corriente.
                        if (self.pin_current.value()):
                            # Onda en semi ciclo negativo.
                            
                            # QUESTION: validar si al desconectar un puente de SCR y conectar en elevacion funciona aca en este estamento.
                            while self.pin_current.value():
                                pass
                            sleep_us(100)
                            if(not self.pin_voltaje.value()):
                                self.scr_120.value(1)
                                self.scr_act = "120"
                        else:
                            # Onda en semi ciclo positivo.
                            # Mi idea es esperar a que la misma pase por cero, una vez allo espear a que pase en elevacion.
                            while not self.pin_current.value():
                                # Una vez salga bucle estara en el semi ciclo negativo.
                                pass
                            
                            while self.pin_current.value():
                                # Una vez entre aca se encontrara en semiciclo negativo
                                pass
                            
                            sleep_us(100)
                            if(not self.pin_voltaje.value()):
                                self.scr_120.value(1)
                                self.scr_act = "120"
                           
                        self.mod1.value(1)
                        self.mod2.value(0)
                        while not self.button.value():
                            # sleep_us(3)
                            pass
                        
                    # 150V        
                    elif(self.cont_btn == 2):
                        self.mod1.value(0)
                        self.mod2.value(1)
                        self.cont_btn == 3
                        while not self.button.value():
                            # sleep_us(3)
                            pass

        
        
            
                
            
             
#SCRPlanta().mainCOMP()            
                
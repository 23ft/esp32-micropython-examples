from machine import Pin
from utime import sleep_us, sleep_ms


button = Pin(15, Pin.IN)
mod1 = Pin(33, Pin.OUT)  # 120V
mod2 = Pin(32, Pin.OUT)  # 150V


cont = 0
contdeb = 0
while True:
    if(not button.value()):
        """
            * Anti rebote algorithm:
                -> BUtton en configuracion PULL-UP
                -> Se realiza deteccion de estado LOW, una vez se realiza la deteccion
                se hace polling para determinar cada < 50us*1300veces > el valor de la señal (se aumenta un contador cada vez que sea LOW)
                -> una vez relizado el sondeo se valida que si el valor es mayor a 700 (valor ajustado en practica) ejecute el cambio.

        """
        contdeb = 0
        for x in range(0, 1300, 1):
            if(not button.value()):
                contdeb += 1
                sleep_us(40) # *El toggle lo detecta sin problemas con un sondeo cada 50us
                # sleep_us(80) *El toggle se ve con delay ademas no es placentero el pulsar el botont
        if(contdeb >= 700):

            cont += 1

            if (cont == 3):
                cont = 1
            
            # Modes.
            
            # 120V    
            if(cont == 1):
                """ 
                    *Preguntar cual esta encendido y apagarlo cuando la señal de voltaje este en elevacion.
                    *Una vez apagado esperar a que la señal de voltaje pase a abatimiento, estando hay esperar
                    a corriente cruze en elevacion cuando cruza esperar 90us para encender nuevos SCRS.
                """
                mod1.value(1)
                mod2.value(0)
                while not button.value():
                    # sleep_us(3)
                    pass

            # 150V        
            elif(cont == 2):
                mod1.value(0)
                mod2.value(1)
                cont == 3
                while not button.value():
                    # sleep_us(3)
                    pass

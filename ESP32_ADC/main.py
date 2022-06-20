# Voltage presente en divisor max 2.50V
# configuracion ADC para test bateria ion litio verde.


from machine import ADC, Pin



pinADC = Pin(13, Pin.ANALOG)
buff = ADC(pinADC, ADC.ATTN_11DB)


while(1):
    print(buff.read_uv())
    
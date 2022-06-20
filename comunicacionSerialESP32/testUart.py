from machine import UART
#import uos
import time 

uart1 = UART(1, baudrate=115200, tx=1, rx=3)
cont = 0
while True:
    uart1.write(b'hello')  # write 5 bytes
    time.sleep(3)
        

        
    
#uart1.read(5)         # read up to 5 bytes


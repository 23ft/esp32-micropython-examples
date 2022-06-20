import serial
import time


com = serial.Serial(port="/dev/ttyUSB0", bytesize=8, baudrate=115200)

while 1:
    com.write('red\0'.encode())
    print("send..\n")
    #ss = com.read(5)
    #print("recive: {ssx}\n".format(ssx= type(ss)))
    time.sleep(5)
    #break
    


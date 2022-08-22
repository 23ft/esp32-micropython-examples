import socket
import time
import sys

# root@198.58.99.52

HOST = "192.168.20.25"  # Standard loopback interface address (localhost)
PORT = 1200  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"cliente 1")
    #data = s.recv(1024)
    try:
        while True:

            sms = input("Ingresa texto a enviar [cliente 1]: ")
            if sms == "stop_flag":
                sms = bytes(sms, 'utf-8')
                s.sendall(sms)
                s.close()
                sys.exit()    
            else:
                sms = bytes(sms, 'utf-8')
                s.sendall(sms)
                data = s.recv(1024)
                print("[server response]: " + data.decode('utf-8'))
                
            
            
            
    finally:
        s.close()
        sys.exit()
        
        
    
#print("recibido: ",data)
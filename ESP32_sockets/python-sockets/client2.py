import socket
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"cliente 2")
    #data = s.recv(1024)
    try:
        while True:

            sms = input("Ingresa texto a enviar [cliente 2]: ")
            sms = bytes(sms, 'utf-8')
            s.sendall(sms)
    finally:
        s.close()
        
        
    
#print("recibido: ",data)
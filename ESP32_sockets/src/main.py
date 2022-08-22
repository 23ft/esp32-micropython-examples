
import usocket as socket
import gc
import utime

HOST = "198.58.99.52"  # Standard loopback interface address (localhost)
PORT = 1200  # Port to listen on (non-privileged ports are > 1023)


try:
    #gc.collect()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(b"SALUODS ESP32")
    
    while True:    
        data = s.recv(1024)
        if data:
            print("recibed data: ", data)
finally:
    pass
    gc.collect()
    s.sendall(b'stop_flag')
    utime.sleep(1)
    s.close()
    

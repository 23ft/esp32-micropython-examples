import socket
import sys

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 1200  # Port to listen on (non-privileged ports are > 1023)
conn = None
adrr = None


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
     
    try:    
        while True:
            #print("[debug] value conn for test-> ", conn)

            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)

                    if data:
                       if data == b'stop_conn':
                           print("\nSTOP CONNECTION WITH -> ", addr)
                           del(conn)
                           break  
                       else: 
                           print("data: ", data)
                           conn.sendall(data)
    finally:
        print("\n[finally] try close server...")
        s.close()
        print("[finally] server is closed\n")
        sys.exit() 
        
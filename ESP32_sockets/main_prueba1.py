# Lanzamos peticion POST por medio de sockets a archivo PHP.

import socket


class Sendinfophp():
    def __init__(self, hosting, port, data):
        self.host = hosting
        self.port = port
        self.data = data
        if self.Createsocket():
            print("Socket creado")
            self.POSTencode()
            self.Request()

    def Createsocket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((str(self.host), int(self.port)))

        return True

    def POSTencode(self):

        self.headers = """\
POST /pruebaproces.php HTTP/1.1\r
Content-Type: {content_type}\r
Content-Length: {content_length}\r
Host: {host}\r
Connection: close\r
\r\n"""


        self.body = self.data.encode('ascii')

        self.header = self.headers.format(
            content_type="application/x-www-form-urlencoded",
            content_length=len(self.body),
            host=str(self.host) + ":" + str(self.port)
        ).encode('iso-8859-1')

        self.MessagePOST = self.header + self.body

    def Request(self):

        self.s.sendall(self.MessagePOST)
        print(self.MessagePOST)
        self.serverrequest = self.s.recv(1024)
        if self.serverrequest:
            print(self.serverrequest)
            self.s.close()
            print("\n\nCERRADO")
        else:
            print("No hubo respuesta del servirdor, error")


host = 'localhost'
port = 8000
data = 'seriex=9&tempx=98'

send = Sendinfophp(host, port, data)

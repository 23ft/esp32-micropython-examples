import logging
import sys
import socketserver
from socketserver import StreamRequestHandler
from time import ctime

# logging utilizado para debug.
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s: %(message)s',
                    )

# Manejador peticiones de serivdor.
class EchoRequestHandler(StreamRequestHandler):

    def __init__(self, request, client_address, server):
        self.logger = logging.getLogger('EchoRequestHandler')
        self.logger.debug('__init__')
        StreamRequestHandler.__init__(self, request,
                                                 client_address,
                                                 server)
        return

    # Se reescriben metodos de la clase socketserver.BaseRequestHandler.
    
    def setup(self):
        return super().setup()
        #self.logger.debug('setup')
        #return BaseRequestHandler.setup(self)

    def handle(self) -> None:
       client_ip = self.client_address[0]
       print("connected from " + client_ip)
       # The readline() function will return only when the client send a \n which is a new line character.
       # If the client do not send the \n character, then readline() mehtod will hang and never return.
       client_send_data_line = self.rfile.readline().strip()
       client_send_data_line_str = client_send_data_line.decode('utf-8')
       print('client_send_data_line : ' + client_send_data_line_str)
       curr_time = ctime()
       self.wfile.write((curr_time + ' - ' + client_send_data_line_str).encode('utf-8'))

    def finish(self):
        return super().finish()
        #self.logger.debug('finish')
        #return BaseRequestHandler.finish(self)
    
# servidor TCP.    
class EchoServer(socketserver.TCPServer):

    def __init__(self, server_address,
                 handler_class=EchoRequestHandler,
                 ):
        self.logger = logging.getLogger('EchoServer')
        self.logger.debug('__init__')
        socketserver.TCPServer.__init__(self, server_address,
                                        handler_class)
        

    
    
address = ('localhost', 65432 )  # let the kernel assign a port
server = EchoServer(address, EchoRequestHandler)
ip, port = server.server_address  # what port was assigned?

with server as s:
    try:
        s.serve_forever()
    finally:
        s.socket.close()
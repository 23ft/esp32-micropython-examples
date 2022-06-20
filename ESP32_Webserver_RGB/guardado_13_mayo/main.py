from machine import Pin, PWM
from time import sleep
import _thread


class RGB:
    def __init__(self):
        self.frec = 1000
        self.green = PWM(Pin(5), self.frec)
        self.red = PWM(Pin(18), self.frec)
        self.blue = PWM(Pin(19), self.frec)
    
    def Secuencia1(self):
            
                print('\n Secuecnia 1\n')
                green = self.green
                red = self.red
                blue = self.blue
                
                green.duty(255)
                red.duty(0)
                blue.duty(255)
                sleep(1)
                green.duty(127)
                red.duty(127)
                blue.duty(127)
                sleep(1)    
                green.duty(0)
                red.duty(255)
                blue.duty(0)
                sleep(1)
                return

class WebServer(RGB):
    def __init__(self):
        RGB.__init__(self)
        self.Createsocket()
        self.Run()
        
        
    def web_page(self):
        
        led_state = 'puto'
        
        html = """<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        .button {
            background-color: #ce1b0e;
            width: 150px;
            height: 60px;
            border: none;
            color: black;
            padding: 16px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }

        .button1 {
            background-color: #0a0;
        }
        
        .button2 {
            background-color: #00a;
        }
        
                .switch {
            position: relative;
            display: inline-block;
            width: 120px;
            height: 68px
        }

        input {
            background-color: black;
        }

        .switch input {
            display: none
        }  

        .slider {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            border-radius: 34px
        }

         .slider:before {
            position: absolute;
            content: "";
            height: 52px;
            width: 52px;
            left: 8px;
            bottom: 8px;
            background-color: #fa0;
            -webkit-transition: .4s;
            transition: ease-in .4s;
            border-radius: 68px 
        }

        input:checked + .slider {
            background-color: #000
        }

        input:checked + .slider:before {
            -webkit-transform: translateX(52px);
            -ms-transform: translateX(52px);
            transform: translateX(52px);
            background-color: #ccc;
        }   
        
        
    </style>
    <script>
        function toggleCheckbox(element) {
                var xhr = new XMLHttpRequest(); if (element.checked) { xhr.open("GET", "/?secuencia1=on", true); }
                else { xhr.open("GET", "/?secuencia1=off", true); } xhr.send();
            }
    </script>
    
</head>

<body>
    <h2> ESP32 - RGB Controller </h2>
    <p>nota: <strong>""" + led_state + """</strong></p>
    <p>
        <i class="fas fa-lightbulb fa-3x" style="color:#c81919;"></i>
        <a href = "/?red_mode"> <button class="button">Red Mode</button> </a>
    </p>
    <p>
        <i class="far fa-lightbulb fa-3x" style="color:#0a0;"></i>
        <a href="/?green_mode"><button class="button button1">Green Mode</button></a>
    </p>
        <p>
        <i class="far fa-lightbulb fa-3x" style="color:#00a;"></i>
        <a href="/?blue_mode"><button class="button button2">Blue Mode</button></a>
    </p>
        
    <label class="switch">
        <input type="checkbox" onchange="toggleCheckbox(this)" %s>
        <span class="slider"></span>
    </label>
</body>

</html>"""
        return html
    
    def Createsocket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', 80))
        self.s.listen(5)
        
    def Request(self):
        try: 
            self.conn, self.addr = self.s.accept()
            self.conn.settimeout(3.0)
            print('\n\n\n ----- Conection ----- \n\n > Conectandose desde: ', str(self.addr))
            self.request = self.conn.recv(1024)
            self.conn.settimeout(None)
            self.request = str(self.request)
            print('\n\n Contenido = \n\n', self.request)
            
            
            self.redmode = '/?red_mode'
            self.greenmode = '/?green_mode'
            self.bluemode = '/?blue_mode'
            self.secuencia1 = '/?secuencia1=on'
            
            self.response = self.web_page()
            self.conn.send('HTTP/1.1 200 OK\n')
            self.conn.send('Content-Type: text/html\n')
            self.conn.send('Connection: close\n\n')
            self.conn.sendall(response)
            self.conn.close()
            
            
            
    def Run(self):
        _thread.start_new_thread(self.Request(), ())      
        while True:
            try:
                if gc.mem_free() < 102000:
                    gc.collect()
                    
                

                if (self.secuencia1 in self.request):
                    print('\n\n >>> Secuencia 1 Activa')
                    self.Secuencia1()
               
                if self.greenmode in self.request:
                    print('\n\n >>> GREEN ON')
                    self.red.duty(0)
                    self.green.duty(255)
                    self.blue.duty(0)
                    
                if self.bluemode in self.request:
                    print('\n\n >>> BLUE ON')
                    self.red.duty(0)
                    self.green.duty(0)
                    self.blue.duty(255)
                       
                
                self.Send()

            except OSError as e:
                self.conn.close()
                print('Conexion cerrada en Webserver.Run()')
                

                                 
#tira = RGB()

serv = WebServer()


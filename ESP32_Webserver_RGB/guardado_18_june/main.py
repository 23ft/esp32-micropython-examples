from machine import Pin, PWM
from time import sleep
import _thread

global breakprogram

class RGB:
    def __init__(self):
        global breakprogram
        self.frec = 1000
        self.green = PWM(Pin(5), self.frec)
        self.red = PWM(Pin(18), self.frec)
        self.blue = PWM(Pin(19), self.frec)
        self.indicador = Pin(2, Pin.OUT)
        
    def BlueMode(self):
        self.indicador.value(not self.indicador.value())
        self.red.duty(0)
        self.green.duty(0)
        self.blue.duty(1023)
        sleep(1)
    
    def GreenMode(self):
        self.indicador.value(not self.indicador.value())
        self.red.duty(0)
        self.green.duty(1023)
        self.blue.duty(0)
        sleep(1)
    
    def RedMode(self):
        self.indicador.value(not self.indicador.value())
        self.red.duty(1023)
        self.green.duty(0)
        self.blue.duty(0)
        sleep(1)
        
    def FullMode(self):
        self.indicador.value(not self.indicador.value())
        self.red.duty(1023)
        self.green.duty(1023)
        self.blue.duty(1023)
        sleep(1)
        
    def Secuencia2(self):
        global breakprogram
        
        self.indicador.value(not self.indicador.value())
        
        for signal_ in range(0,1023,100):
            self.red.duty(signal_)
            self.blue.duty(signal_)
            self.green.duty(signal_)
            sleep(0.5)
            
        for signal_2 in range(1023, 0, -100):
            self.red.duty(signal_2)
            self.blue.duty(signal_2)
            self.green.duty(signal_2)
            if breakprogram == 1:
                print('rompiendo for 2')
                breakprogram = 0
                break
            sleep(0.5)
        
    def Secuencia1(self):
        global breakprogram
        
        self.indicador.value(not self.indicador.value())
        colors = [1023, 700, 500, 255, 200, 150, 100, 50]
        
        for signal in colors:
            self.red.duty(signal)
            self.green.duty(signal)
            self.blue.duty(signal)
            if breakprogram == 1:
                breakprogram = 0
                break
            sleep(0.05)
                    
        for signal2 in range((len(colors)-1), 0, -1):
            self.red.duty(colors[signal2])
            self.green.duty(colors[signal2])
            self.blue.duty(colors[signal2])
            if breakprogram == 1:
                breakprogram = 0
                break
            sleep(0.05)
                     
    def Stop(self):
        breakprogram = 0
        self.red.duty(0)
        self.green.duty(0)
        self.blue.duty(0)
        self.indicador.value(1)
        sleep(1)
        
class WebServer(RGB):
    def __init__(self):
        RGB.__init__(self)
        self.Createsocket()
        self.Run()
      
    def web_page(self):
        
        instagram = 'Created By @23ft'
        
        html = """<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        * {
            box-sizing: border-box;
            padding: 0;
        }

        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            /* text-align: center; */
            
        }

        body {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #111;
        }


        /* Contenedor princiapl = Control RGB */
        .controll{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-items: center;
            border-radius: 30px;
            border: #ccc 1.3px solid;
            padding: 2.5vh 2vw;
            background-color:rgb(214, 211, 211);
        }

        /* Contenedor hijo = Seccion titulo */
        .title{
            color: #cdc;
            display: flex;
            flex-direction: column;
            width: 24vw;
            border: 1px solid #ccc;
            padding: 5px;
            border-radius: 15px;
            margin-bottom: 5px;
            align-items: center;
            justify-items: center;
            background-color: #000;
        }

        .title h2 {
            font-size: 1.5vw;
            /* border: 2px solid white; */
            margin: 0;
        }

        .title p {
            /* border: 2px solid white; */
            font-style: oblique;
            font-family: 'Courier New', Courier, monospace;
            font-weight: bold;
            font-size: 1vw;
            color: tomato;
            margin-top: -1px;
            margin-bottom: 0;
        }


        /* Contenedor hijo = Seccion botones */
        .controll .botones {
            display: flex;
            flex-direction: row;
            border-radius: 15px;
            border: #eee 1px solid;
            width: 24vw;
            padding: .5vw;
            align-items: center;
            justify-content: center;
            background-color: #000;


        }

        /* Contenedor hijo = Seccion switches */
        .switches {
            display: flex;
            flex-direction: column;
            justify-items: center;
            align-items: center;
            border-radius: 15px;
            border: #eee 1px solid;
            width: 24vw;
            background-color: #000;
            padding: .5vw;   
        }

        /* Botones */
        .botons {
            margin: 1vh 1vw 1vh 1vw;
            padding: .3vh .3vw;
        }

        .botons a {
            text-decoration: none;
        }
        
        .button {
            width: 3vw;
            /* height: 6vh; */
            border: #fcf;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            margin: 3vh 0px 3vh 0px;
            padding: 2vh 1.5vw;
        }
        /* Red Mode Buttons */
        .button1 {
            background-color: #f00;
            border-radius: 1em;
        }

        /* rgb(204, 102, 0) */
        .button1_2 { 
            background-color: #cc6600; 
            border-radius: 1em;
        }

        /* rgb(255, 153, 0) */
        .button1_3 {
            background-color: #ff9900;
            border-radius: 1em;
        }

        /* rgb(204, 153, 0) */
        .button1_4 {
            background-color: #cc9900;
            border-radius: 1em;
        }

        /* rgb(255, 255, 0) */
        .button1_5 {
            background-color: #ffff00;
            border-radius: 1em;
        }
        
        /* Green Mode Buttons */
        .button2 {
            background-color: #0f0;
            border-radius: 1em;
        }

        /* rgb(0, 204, 0) */
        .button2_1 {
            background-color: #00cc00;
            border-radius: 1em;
        }

        /* rgb(0, 204, 102) */
        .button2_2 {
            background-color: #00cc66;
            border-radius: 1em;
        }

        /* rgb(0, 204, 153) */
        .button2_3 {
            background-color: #00cc99;
            border-radius: 1em;
        }

        .button2_4 {
            background-color: #339966;
            border-radius: 1em;
        }
        
        /* BLue Mode Buttons */
        .button3 {
            background-color: rgb(0, 0, 255);
            border-radius: 1em;
        }

        /* rgb(0, 0, 153) */
        .button3_1 {
            background-color: #000099;
            border-radius: 1em;
        }

        /* rgb(51, 51, 153) */
        .button3_2 {
            background-color: #333399;
            border-radius: 1em;
        }

        /* rgb(102, 0, 204) */
        .button3_3 {
            background-color: #6600cc;
            border-radius: 1em;
        }

        /* rgb(153, 102, 255) */
        .button3_4 {
            background-color: #9966ff;
            border-radius: 1em;
        }

        /* Button stop */
        .button4 {
            background-color: #600;
            border-radius: 1em;
        }

        .button4_1 {
            background-color: white;
            border-radius: 1em;
        }

        /* rgb(255, 153, 255) */
        .button4_2 {
            background-color: #ff99ff;
            border-radius: 1em;
        }

        /* rgb(255, 102, 255) */
        .button4_3 {
            background-color: #ff66ff;
            border-radius: 1em;
        }

        /* rgb(153, 204, 255) */
        .button4_4 {
            background-color: #99ccff;
            border-radius: 1em;
        }

        /* Iconos */
        .icons {
            font-size: 2.5vw;
        }
        
        /* Switches interactivos */

        /* Contenedor switches */
        
        .switchcontainer{
            display: flex;
            flex-direction: row;
            color: white;
            /* border:2px solid white; */
            align-items: center;
            justify-items: center;
            
        }

        /* Caracteristicas generales nombre switch */
        .secs {
            /* outline: 2px solid white; */
            width: 10vw;
            font-size: 1.5vw;
            font-weight: bold;
        }

        /* Caracterisitcias generales switch */
        .switch {
           width: 4.5vmax;
           height: 2.7vmax;
                      
        }

        input {
            background-color: black;
        }

        .switch input {
            display: none
        }  

        .slider {
            position: absolute;
            width: 4vmax;
            height: 2.5vmax;
            background-color: #ccc;
            border-radius: 1em;
            transition: ease-in .10s;
        }

        .slider:before {
            position: absolute;
            content: "";
            height: 2vmax;
            width: 2vmax;
            margin: .3vmax 0em 0em .4vmax;
            background-color: rgb(255, 167, 5);
            -webkit-transition: .4s;
            transition: ease-in .4s;
            border-radius: 2em;
        }

        input:checked + .slider {
           background-color: #aaf; 
        }

        input:checked + .slider:before {
            -webkit-transform: translateX(1.5px);
            -ms-transform: translateX(1.5px);
            transform: translateX(1.5vw);
            background-color: #0f0;
        }   
        
        
    </style>
    <script>
        function secuencia1(element) {
                var xhr = new XMLHttpRequest(); if (element.checked) { xhr.open("GET", "/?secuencia1=on", true); }
                else { xhr.open("GET", "/?secuencia1=off", true); } xhr.send();
            }
        function secuencia2(element2) {
                var xhr2 = new XMLHttpRequest(); if (element2.checked) { xhr2.open("GET", "/?secuencia2=on", true); }
                else { xhr2.open("GET", "/?secuencia2=off", true); } xhr2.send();
            }
    </script>
    
</head>

<body>

    <div class="controll">
        <div class="title"> 
            <h2> ESP32 - RGB Controller </h2>
            <p><strong>""" + instagram + """</strong></p> 
        </div>
        <div class="botones">
            <div class="botons botons1">

                <a href = "/?red_mode"> <button class="button button1">   <i class="far fa-lightbulb fa-3x icons icono1"> </i> </button> </a>
                <a href = "/?red_mode1"> <button class="button button1_2">   <i class="far fa-lightbulb fa-3x icons icono1"> </i> </button> </a>
                <a href = "/?red_mode2"> <button class="button button1_3">   <i class="far fa-lightbulb fa-3x icons icono1"> </i> </button> </a>
                <a href = "/?red_mode3"> <button class="button button1_4">   <i class="far fa-lightbulb fa-3x icons icono1"> </i> </button> </a>
                <a href = "/?red_mode4"> <button class="button button1_5">   <i class="far fa-lightbulb fa-3x icons icono1"> </i> </button> </a>
            </div>
            <div class="botons botons2">

                <a href="/?green_mode"> <button class="button button2"> <i class="far fa-lightbulb fa-3x icons icono2" > </i> </button> </a>
                <a href="/?green_mode1"> <button class="button button2_1"> <i class="far fa-lightbulb fa-3x icons icono2" > </i> </button> </a>
                <a href="/?green_mode2"> <button class="button button2_2"> <i class="far fa-lightbulb fa-3x icons icono2" > </i> </button> </a>
                <a href="/?green_mode3"> <button class="button button2_3"> <i class="far fa-lightbulb fa-3x icons icono2" > </i> </button> </a>
                <a href="/?green_mode4"> <button class="button button2_4"> <i class="far fa-lightbulb fa-3x icons icono2" > </i> </button> </a>
            </div>
            <div class="botons botons3">

                <a href="/?blue_mode"> <button class="button button3"> <i class="far fa-lightbulb fa-3x icons icono3"> </i>  </button> </a>
                <a href="/?blue_mode1"> <button class="button button3_1"> <i class="far fa-lightbulb fa-3x icons icono3"> </i>  </button> </a>
                <a href="/?blue_mode2"> <button class="button button3_2"> <i class="far fa-lightbulb fa-3x icons icono3"> </i>  </button> </a>
                <a href="/?blue_mode3"> <button class="button button3_3"> <i class="far fa-lightbulb fa-3x icons icono3"> </i>  </button> </a>
                <a href="/?blue_mode4"> <button class="button button3_4"> <i class="far fa-lightbulb fa-3x icons icono3"> </i>  </button> </a>
            </div>  
            <div class="botons botons4">

                <a href="/?stop"><button class="button button4">  <i class="fas fa-ban icons icono4"></i> </button> </a>
                <a href="/?white_mode1"><button class="button button4_1">  <i class="far fa-lightbulb fa-3x icons icono4"></i> </button> </a>
                <a href="/?white_mode2"><button class="button button4_2">  <i class="far fa-lightbulb fa-3x icons icono4"></i> </button> </a>
                <a href="/?white_mode3"><button class="button button4_3">  <i class="far fa-lightbulb fa-3x icons icono4"></i> </button> </a>
                <a href="/?white_mode4"><button class="button button4_4">  <i class="far fa-lightbulb fa-3x icons icono4"></i> </button> </a>

            </div>
        </div>
        <div class="switches">
            <div class="switch1 switchcontainer">
                <p class="secs"> Secuencia 1 </p>
                <label class="switch">
                    <input type="checkbox" onchange="secuencia1(this)" %s>
                    <span class="slider"></span>
                </label>
            </div>
            <div class="switch2 switchcontainer">
                <p class="secs"> Secuencia 2 </p>
                <label class="switch">
                    <input type="checkbox" onchange="secuencia2(this)" %s>
                    <span class="slider"></span>
                </label>
            </div>  
        </div>
    </div>
</body>

</html>"""
        return html
    
    def Createsocket(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', 80))
        self.s.listen(5)
        
    def Request(self):
        global breakprogram
        breakprogram = 0
        while True:
            try:
                # Lectura HttpRequest.
                self.conn, self.addr = self.s.accept()
                self.conn.settimeout(3.0)
                print('\n\n\n ----- Conection ----- \n\n > Conectandose desde: ', str(self.addr))
                self.request = self.conn.recv(1024)
                self.conn.settimeout(None)
                self.request = str(self.request)
                print('\n\n Contenido = \n\n', self.request)
                
                #stop program.
                if self.request.find(self.values['stopbreak']) == 6:
                    breakprogram = 1
                    break

                self.response = self.web_page()
                self.conn.send('HTTP/1.1 200 OK\n')
                self.conn.send('Content-Type: text/html\n')
                self.conn.send('Connection: close\n\n')
                self.conn.sendall(self.response)
                self.conn.close()
            except:
                self.conn.close()
                print('error')
                
            
    # Method 'principal'.                       
    def Run(self):
        global breakprogram
        
        # First Thread: Httprequest for page
        _thread.start_new_thread(self.Request, ())
        
        # Second Thread: Secuences in the led strip.
        while True:
            try:
                
                self.values = {'redmode':'/?red_mode',
                          'greenmode':'/?green_mode',
                          'bluemode':'/?blue_mode',
                          'sec1on': '/?secuencia1=on',
                          'sec1off': '/?secuencia1=off',
                          'sec2on': '/?secuencia2=on',
                          'sec2off': '/?secuencia2=off',
                          'stopbreak':'/?stop' }
                
                self.redmode = '/?red_mode'
                self.greenmode = '/?green_mode'
                self.bluemode = '/?blue_mode'
                self.secuencia1 = '/?secuencia1=on'
                self.secuencia1off = '/?secuencia1=off'
                self.stopbreak = '/?stop'
                
                gc.collect() if gc.mem_free() < 102000 else None
                
                #Secuencias.
                self.Secuencia1() if self.request.find(self.values['sec1on']) == 6 else None        
                self.Stop() if self.request.find(self.values['sec1off']) == 6 else None
                
                self.Secuencia2() if self.request.find(self.values['sec2on']) == 6 else None
                self.Stop() if self.request.find(self.values['sec2off']) == 6 else None
                
                #Modos.
                self.GreenMode() if self.request.find(self.values['greenmode']) == 6 else None    
                self.BlueMode() if self.request.find(self.values['bluemode']) == 6 else None
                self.RedMode() if self.request.find(self.values['redmode']) == 6 else None
                
                #stop program.
                if breakprogram == 1:
                    self.Stop()
                    print('\n\n >> Parada programada para pruebas - Bugs Editor :V \n\n ')
                    break
            except:
                continue
            
# Start of the program!                                 
page = WebServer()
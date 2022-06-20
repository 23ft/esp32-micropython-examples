from PySide6 import QtCore, QtWidgets, QtGui
import serial

# creamos clase a la cual heredamos objeto QPushButton
class btns(QtWidgets.QPushButton):
    def __init__(self, bgColor, bdColor):
        super().__init__()
        self.com = serial.Serial(port="/dev/ttyUSB0", bytesize=8, baudrate=115200)
        self.bdcolor = bdColor
        self.bgcolor = bgColor
        self.setFixedSize(QtCore.QSize(100, 100))
        self.setContentsMargins(10,10,10,10)
        self.setStyleSheet("""
                           opacity: -1;
                           border-radius : 50%; 
                           border : 2px solid {bdcolor}; 
                           background-color: {bgcol};
                           """.format(bgcol=self.bgcolor, bdcolor = self.bdcolor))
        self.clicked.connect(self.func)
        self.cont = 0
        
    def func(self):
        
        if not self.cont:
            #self.__init__()
            print("CHECK {COOR}".format(COOR=self.bgcolor))
            self.setStyleSheet("""
                           border-radius : 50%; 
                           border : 4px solid white; 
                           background-color: {bgcol};
                           """.format(bdcolor=self.bdcolor, bgcol = self.bgcolor))
            self.setText("Check") 
            self.cont = 1
            
            if self.bgcolor == "red":
                self.com.write("red".encode())
                
            elif self.bgcolor == "yellow":
                self.com.write("yellow".encode())
            
            elif self.bgcolor == "green":
                self.com.write("green".encode())
        else:
            print("UNCHECK {COOR}".format(COOR=self.bgcolor))
            self.setStyleSheet("""
                           border-radius : 50%; 
                           border : 2px solid {bdcolor}; 
                           background-color: {bgcol};
                           """.format(bdcolor=self.bdcolor, bgcol = self.bgcolor))
            self.setText("Uncheck")
            self.cont = 0
            
class Semaforo(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mask = QtWidgets.QGridLayout()
        self.setAutoFillBackground(True)
        self.setFixedSize(QtCore.QSize(250,350))

        
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor("black"))
        self.setPalette(palette)
        
        self.mask.addWidget(btns(bgColor="red", bdColor="red"), 0, 0)
        self.mask.addWidget(btns(bgColor="yellow", bdColor="yellow"), 1, 0)
        self.mask.addWidget(btns(bgColor="green", bdColor="green"), 2, 0)
        self.setLayout(self.mask)   

class Gui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Semaforo electiva 1")
        self.setFixedSize(QtCore.QSize(500,600))
        
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(Semaforo(), 0, 0)
        
        child = QtWidgets.QWidget()
        child.setLayout(self.layout)
        self.setCentralWidget(child)

    
app = QtWidgets.QApplication()
gui = Gui()
gui.show()
app.exec()
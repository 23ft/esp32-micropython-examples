import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtWidgets, QtGui

def normalParadigm():
    
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QMainWindow()
    window.show()

    # Start the event loop.
    app.exec()
    
class Color(QtWidgets.QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        self.setFixedSize(QtCore.QSize(300,300))

        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
        self.setPalette(palette)
        print("in color: ", QtGui.QPalette.Window)
    
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.btn = QtWidgets.QPushButton("Press")
        
        layout = QtWidgets.QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(self.btn, 2, 2)
        
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QtCore.QSize(1000,1000))
        print("in main: ", QtGui.QPalette.Window)

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prueba")
        
        
        self.setCentralWidget(self.btn)
        self.setFixedSize(QtCore.QSize(700,700))
        self.show()
        
app = QtWidgets.QApplication()
win = MainWindow()
win.show()
app.exec()


import sys
import cv2
from PyQt6.QtCore import QSize, Qt, QObject, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QLabel , QMainWindow, QPushButton,QGridLayout
from PyQt6.QtGui import QPixmap, QImage

from  control import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Orereco")

        self.setFixedSize(QSize(900, 600))

        layout = QGridLayout()

        button = QPushButton("Work")
        
        button2 = QPushButton("OpenFile")

        button.clicked.connect(self.analyse)
        button2.clicked.connect(self.open)

        #self.setCentralWidget(button)
        
        self.img = QLabel("hello")

        

        

        layout.addWidget(button,0,0)
        layout.addWidget(self.img,0,1)
        layout.addWidget(button2,1,0)





        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def analyse(self):
        im = cont.analyseShot()
        self.img.setPixmap(QPixmap.fromImage(im).scaled(640,480))
        #self.setCentralWidget(self.img)
        self.img.show()

    def open(self):
        cont.selectSource()
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
import sys
import cv2
from PyQt6.QtCore import QSize, Qt, QObject, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QLabel , QMainWindow, QPushButton,QVBoxLayout
from PyQt6.QtGui import QPixmap, QImage

from  control import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Orereco")

        self.setFixedSize(QSize(900, 600))

        button = QPushButton("Press")

        self.setCentralWidget(button)
        
        self.img = QLabel("hello")

        button.clicked.connect(self.the_button_was_clicked)

        layout = QVBoxLayout()

        layout.addWidget(button)
        layout.addWidget(self.img)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        im = cont.analyseShot()
        self.img.setPixmap(QPixmap.fromImage(im).scaled(640,480))
        #self.setCentralWidget(self.img)
        self.img.show()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()